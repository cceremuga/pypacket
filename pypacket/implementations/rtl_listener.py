from subprocess import Popen, PIPE, STDOUT
from pypacket.framework.listener import Listener


class RtlListener(Listener):
    def load(self, config, log_handler):
        log_handler.log_info('Starting listener subprocess, listening on {0}.'.format(config.frequency()))

        # Start listener subprocess which listens for APRS packets.
        return Popen(
            ['rtl_fm', '-M', 'fm', '-f', config.frequency(), '-s',
            config.sample_rate(), '-l', '0', '-g', config.gain(), '-'],
            stdout=PIPE, stderr=STDOUT
        )
