from pypacket.base.processor import ProcessorBase


class MockProcessor(ProcessorBase):
    def __init__(self):
        self.log_handler = None

    def load(self, config, log_handler):
        self.log_handler = log_handler
        log_handler.log_info('Starting mock processor.')

    def handle(self, packet):
        self.log_handler.log(packet)
