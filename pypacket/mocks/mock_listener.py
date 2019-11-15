from pypacket.framework.listener import Listener


class MockListener(Listener):
    def load(self, config, log_handler):
        log_handler.log_info('Starting mock listener subprocess.')
