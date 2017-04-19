import threading
import subprocess
import re
import sys
from pypacket.util.logger import Logger

class Listener:
    def __init__(self, log_handler, config):
        self.config = config
        self.log_handler = log_handler
        self.sub_processes = {}
        self.start()
        self.is_running = True
        self.worker_thread = threading.Thread(target=self.multimon_worker)
        self.worker_thread.setDaemon(True)
        self.worker_thread.start()

    def start(self):
        # Start rtl_fm subprocess which listens for APRS signals.
        self.log_handler.log_info('Starting rtl_fm subprocess.')

        rtl_subprocess = subprocess.Popen(
            ['rtl_fm', '-M', 'fm', '-f', self.config.frequency(), '-s',
            self.config.sample_rate(), '-l', '0', '-g', self.config.gain(), '-'],
            stdout=subprocess.PIPE, stderr=open('/dev/null')
        )

        # Start multimon-ng subprocess which decodes APRS data.
        self.log_handler.log_info('Starting multimon-ng subprocess.')

        multimon_subprocess = subprocess.Popen(
            ['multimon-ng', '-a', 'AFSK1200', '-A', '-t', 'raw', '-'],
            stdin=rtl_subprocess.stdout,
            stdout=subprocess.PIPE, stderr=open('/dev/null')
        )

        # Push subprocesses into collection.
        self.sub_processes['rtl'] = rtl_subprocess
        self.sub_processes['multimon'] = multimon_subprocess

    def stop(self):
        self.sub_processes['rtl'].terminate()
        self.sub_processes['multimon'].terminate()
        self.log_handler.log_info('Exiting!')
        sys.exit(0)

    def process_decoded_packet(self, decoded_packet):
        self.log_handler.log_packet(decoded_packet)

    def clean_decoded_packet(self, decoded_packet):
        # The first 6 characters are not valid APRS packet components.
        aprs_match = re.compile(r'^APRS: (.*)') \
            .match(decoded_packet)
        if aprs_match:
            return aprs_match.group(1)

        return None

    def multimon_worker(self):
        # This worker lives in its own thread and processes received packets.
        self.log_handler.log_info('Worker thread starting, listening.')

        while self.is_running:
            try:
                decoded_packet = self.sub_processes['multimon'] \
                    .stdout.readline().decode('utf-8').strip()

                cleaned_packet = self.clean_decoded_packet(decoded_packet)

                if cleaned_packet is not None:
                    self.process_decoded_packet(cleaned_packet)

            except UnicodeDecodeError:
                self.log_handler.log_warn('Unable to decode packet.')
