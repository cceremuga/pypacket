from pypacket.framework.decoder import Decoder


class MockDecoder(Decoder):
    def load(self, config, log_handler, listener_subprocess):
        log_handler.log_info('Starting mock decoder subprocess.')
