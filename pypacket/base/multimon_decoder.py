import subprocess
from pypacket.base.decoder import DecoderBase


class MultimonDecoder(DecoderBase):
    def load(self, config, log_handler, listener_subprocess):
        log_handler.log_info('Starting decoder subprocess.')

        # Start decoder subprocess which decodes APRS data.
        return subprocess.Popen(
            ['multimon-ng', '-a', 'AFSK1200', '-A', '-t', 'raw', '-'],
            stdin=listener_subprocess.stdout,
            stdout=subprocess.PIPE, stderr=open('/dev/null')
        )
