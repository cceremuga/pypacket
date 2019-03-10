from pypacket.base.processor import ProcessorBase
from threading import Timer
from aprslib.exceptions import (
    ConnectionDrop,
    ConnectionError,
    LoginError
)
import aprslib
import os


class AprsIsProcessor(ProcessorBase):
    def __init__(self):
        """Instantiates the list list of packets, preps the timer."""
        self.packets = []
        self.thread = None
        self.log_handler = None
        self.config = None
        self.is_client = None
        self.timer_seconds = None

    def load(self, config, log_handler):
        """Starts a threaded timer for handling packets in bulk once per minute.

        Args:
            config: The related app configuration.
            log_handler: The log handler for the app.
        """
        self.config = config
        self.timer_seconds = self.config.how_often_to_process()
        self.log_handler = log_handler

        username = self.__get_username()
        password = self.__get_password()
        host = self.config.host()
        self.is_client = aprslib.IS(username, passwd=password, host=host, port=14580)

        try:
            self.__is_connect()
        except LoginError:
            self.log_handler.log_error('Unable to log into APRS-IS with the specified credentials, cannot upload.')
            return
        except ConnectionError:
            self.log_handler.log_info('Unable to connect to APRS-IS.')
            return

        log_handler.log_info('Starting IGate.')
        self.thread = Timer(self.timer_seconds, self.__timer_handle)
        self.thread.start()

    def handle(self, packet):
        """Handles a single packet, adding it to the list.

        Args:
            packet: A decoded packet to add to the list.
        """
        self.packets.append(packet)

    def __timer_handle(self):
        self.__send_packets()

        self.packets.clear()
        self.thread = Timer(self.timer_seconds, self.__timer_handle)
        self.thread.start()

    def __send_packets(self):
        if not self.packets:
            return

        self.log_handler.log_info('Uploading {0} packet(s) to APRS-IS.'.format(len(self.packets)))

        try:
            for packet in self.packets:
                self.is_client.sendall(packet)
        except ConnectionDrop:
            self.__is_reconnect()
            return
        except ConnectionError:
            self.__is_reconnect()
            return

        self.log_handler.log_info('APRS-IS upload complete.')

    def __get_username(self):
        return os.environ.get('PYPACKET_USERNAME', 'setme')

    def __get_password(self):
        return os.environ.get('PYPACKET_PASSWORD', 'setme')

    def __is_reconnect(self):
        self.log_handler.log_warning('Disconnected from APRS-IS, attempting to reconnect.')
        self.__is_connect()

    def __is_connect(self):
        self.log_handler.log_info('Connecting to APR-IS.')
        self.is_client.connect()
