from pypacket.base.processor import ProcessorBase
from threading import Timer
import aprslib


class AprsIsProcessor(ProcessorBase):
    def __init__(self):
        """Instantiates the list list of packets, preps the timer."""
        self.packets = []
        self.thread = Timer(60, self.__timer_handle)
        self.log_handler = None

    def load(self, config, log_handler):
        """Starts a threaded timer for handling packets in bulk once per minute.

        Args:
            config: The related app configuration.
            log_handler: The log handler for the app.
        """
        self.log_handler = log_handler
        log_handler.log_info('Starting IGate processor.')
        self.thread.start()

    def handle(self, packet):
        """Handles a single packet, adding it to the list.

        Args:
            packet: A decoded packet to add to the list.
        """
        self.packets.append(packet)

    def __timer_handle(self):
        if not self.packets:
            self.log_handler.log_info('No packets to send to APRS-IS.')
        else:
            self.__send_packets()

        self.packets.clear()
        self.thread = Timer(60, self.__timer_handle)
        self.thread.start()

    def __send_packets(self):
        self.log_handler.log_info('Connecting to APR-IS.')

        is_client = aprslib.IS('KD2NSP', passwd='22968', port=14580)
        is_client.connect()

        self.log_handler.log_info('Sending {0} packet(s) to APRS-IS.'.format(len(self.packets)))

        for packet in self.packets:
            is_client.sendall(packet)

        self.log_handler.log_info('APRS-IS upload complete.')
