import subprocess
from pypacket.base.listener import ListenerBase


class RtlListener(ListenerBase):
    def load(self, config, log_handler):
        log_handler.log_info('Starting listener subprocess, listening on ' + \
            config.frequency() + '.')

        # Start listener subprocess which listens for APRS packets.
        return subprocess.Popen(
            ['rtl_fm', '-M', 'fm', '-f', config.frequency(), '-s',
            config.sample_rate(), '-l', '0', '-g', config.gain(), '-'],
            stdout=subprocess.PIPE, stderr=open('/dev/null')
        )
