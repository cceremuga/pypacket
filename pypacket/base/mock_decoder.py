import subprocess
from pypacket.base.decoder import DecoderBase

class MockDecoder(DecoderBase):
    def load(self, config, log_handler, listener_subprocess):
        log_handler.log_info('Starting mock decoder subprocess.')
