from pypacket.base.processor import ProcessorBase
from threading import Timer
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

        self.log_handler.log_info('Connecting to APR-IS.')
        self.is_client = aprslib.IS(self.__get_username(), passwd=self.__get_password(), port=14580)
        self.__is_connect()

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

        for packet in self.packets:
            self.is_client.sendall(packet)

        self.log_handler.log_info('APRS-IS upload complete.')

    def __get_username(self):
        return os.environ.get('PYPACKET_USERNAME', 'setme')

    def __get_password(self):
        return os.environ.get('PYPACKET_PASSWORD', 'setme')

    def __is_connect(self):
        self.is_client.connect()
