from pypacket.framework.processor import Processor
from pypacket.framework.beacon import Beacon
from aprslib.exceptions import ConnectionDrop, ConnectionError, LoginError
import aprslib
import datetime


class AprsIsProcessor(Processor):
    def __init__(self):
        """Sets up the functionality we will be using to upload to APRS-IS."""
        self.log_handler = None
        self.config = None
        self.is_client = None
        self.is_connected = False
        self.last_beacon = None

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

        username = self.config.username()
        password = self.config.password()

        if not username or not password:
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
            self.__send_packet(packet)

            # Potentially transmit a beacon.
            self.__send_beacon()
        except ConnectionDrop:
            self.__is_reconnect()
            return
        except ConnectionError:
            self.__is_reconnect()
            return

    def __is_reconnect(self):
        self.log_handler.log_warn('Disconnected from APRS-IS, attempting to reconnect.')
        self.__is_connect()

    def __is_connect(self):
        self.log_handler.log_info('Connecting to APRS-IS.')
        self.is_client.connect()
        self.is_connected = True
        self.log_handler.log_info('Connected as {0}.'.format(self.config.username()))
        self.__send_beacon()

    def __send_beacon(self):
        """ Transmits a beacon on connect if lat/long is set. """
        processor_name = self.get_name()
        latitude = self.config.latitude(processor_name)
        longitude = self.config.longitude(processor_name)

        if not latitude or not longitude:
            return

        # Only send beacon if X minute(s) has passed since last beacon.
        now = datetime.datetime.now()
        minutes_since_beacon = 0

        if self.last_beacon is not None:
            difference = now - self.last_beacon
            minutes_since_beacon = (difference.seconds / 60)

        if self.last_beacon is not None and minutes_since_beacon < self.config.beacon_interval():
            return

        self.log_handler.log_info(
            'Sending IGate beacon for {0} {1}. Another will send in approximately {2} minute(s) when a packet is received.'.
            format(latitude, longitude, self.config.beacon_interval()))

        beacon = Beacon(self.config, self.get_name())
        self.__send_packet(beacon)
        self.last_beacon = datetime.datetime.now()

    def __send_packet(self, packet):
        """Central place for sending packets to the connected client."""
        if self.config.debug_mode():
            return

        self.is_client.sendall(packet)
