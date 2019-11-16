from pypacket.framework.listener import Listener


class MockListener(Listener):
    def load(self, config, log_handler):
        log_handler.log_info('Starting mock listener subprocess.')
        return self

    def wait(self, timeout):
        return 0
