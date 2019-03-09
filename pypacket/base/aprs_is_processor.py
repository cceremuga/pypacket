from pypacket.base.processor import ProcessorBase
from threading import Timer

class AprsIsProcessor(ProcessorBase):
    def __init__(self):
        """Instantiates the list list of packets"""
        self.packets = []
        self.thread = Timer(60, self.__timer_handle)

    def load(self, config, log_handler):
        self.log_handler = log_handler
        log_handler.log_info('Starting processor.')
        self.thread.start()

    def handle(self, packet):
        self.packets.append(packet)

    def __timer_handle(self):
        if not self.packets:
            self.log_handler.log_info('No packets to send to iGate.')
        else:
            self.__send_packets()

        self.packets.clear()
        self.thread = Timer(60, self.__timer_handle)
        self.thread.start()

    def __send_packets(self):
        self.log_handler.log_info('Sending {0} packet(s) to iGate.'.format(len(self.packets)))
        for packet in self.packets:
            self.log_handler.log_info(packet)
