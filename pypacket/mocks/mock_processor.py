from pypacket.framework.processor import Processor


class MockProcessor(Processor):
    def __init__(self):
        self.log_handler = None

    def get_name(self):
        return 'mock'

    def load(self, config, log_handler):
        self.log_handler = log_handler
        log_handler.log_info('Starting mock processor.')

    def handle(self, packet):
        self.log_handler.log(packet)
