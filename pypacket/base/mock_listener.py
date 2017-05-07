import subprocess
from pypacket.base.listener import ListenerBase

class MockListener(ListenerBase):
    def load(self, config, log_handler):
        log_handler.log_info('Starting mock listener subprocess.')
