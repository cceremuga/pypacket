from pypacket.framework.processor import Processor
from aprslib.exceptions import ConnectionDrop, ConnectionError, LoginError
import aprslib
import os


class AprsIsProcessor(Processor):
    def __init__(self):
        """Sets up the functionality we will be using to upload to APRS-IS."""
        self.log_handler = None
        self.config = None
        self.is_client = None
        self.is_connected = False

    def get_name(self):
        """Gets the name of this processor to match against the config."""
        return "aprs-is"

    def load(self, config, log_handler):
        """Connects to APRS-IS to get ready for packet upload.

        Args:
            config: The related app configuration.
            log_handler: The log handler for the app.
        """
        self.config = config
        self.log_handler = log_handler

        username = self.__get_username()
        password = self.__get_password()

        if username is None or password is None:
            self.log_handler.log_warn(
                'Username or password for APRS-IS not set, will not be uploading. See README for more info.')
            return

        host = self.config.host(self.get_name())
        self.is_client = aprslib.IS(username, passwd=password, host=host, port=14580)

        try:
            self.__is_connect()
        except LoginError:
            self.log_handler.log_error('Unable to log into APRS-IS with the specified credentials, cannot upload.')
        except ConnectionError:
            self.log_handler.log_info('Unable to connect to APRS-IS.')

    def handle(self, packet):
        """Handles a single packet, adding it to the list.

        Args:
            packet: A decoded packet to add to the list.
        """
        if not self.is_connected:
            return

        try:
            self.is_client.sendall(packet)
        except ConnectionDrop:
            self.__is_reconnect()
            return
        except ConnectionError:
            self.__is_reconnect()
            return

    def __get_username(self):
        return os.environ.get('PYPACKET_USERNAME')

    def __get_password(self):
        return os.environ.get('PYPACKET_PASSWORD')

    def __is_reconnect(self):
        self.log_handler.log_warn('Disconnected from APRS-IS, attempting to reconnect.')
        self.__is_connect()

    def __is_connect(self):
        self.log_handler.log_info('Connecting to APRS-IS.')
        self.is_client.connect()
        self.is_connected = True
        self.log_handler.log_info('Connected as {0}.'.format(self.__get_username()))
