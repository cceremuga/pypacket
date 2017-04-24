import threading
import subprocess
import re
import sys
from pypacket.util.logger import Logger

class Listener:
    """This is the main listener class for PyPacket. It spawns two subprocesses
    in a separate thread.

    The first subprocess is the rtl_fm listener which listens on the configured
    frequency, sending all raw output to the second subprocess.

    The second subprocess is the multimon-ng decoding process. Once a received
    packet has been decoded, it is cleaned up, leaving the raw APRS String.

    The string is then logged to file and output to the CLI for easy reading.

    Attributes:
        config: The instance of Configuration containing all runtime options.
        log_handler: The instance of Logger containing all logging operations.
        sub_processes: A collection of subprocesses, initialized in start().
        is_running: Indicates whether or not the listener is running.
        worker_thread: A separate thread handling all subprocesses.
    """

    def __init__(self, log_handler, deserializer, config):
        """Initializes the instance of Listener and starts listening."""
        self.config = config
        self.log_handler = log_handler
        self.deserializer = deserializer
        self.sub_processes = {}
        self.__start()
        self.is_running = True
        self.worker_thread = threading.Thread(target=self.__multimon_worker)
        self.worker_thread.setDaemon(True)
        self.worker_thread.start()

    def stop(self):
        """Stops the listener subprocesses, performs a system exit."""
        self.sub_processes['rtl'].terminate()
        self.sub_processes['multimon'].terminate()
        self.log_handler.log_info('Interrupt received, exiting.')
        sys.exit(0)

    def __start(self):
        """Starts the listener, decoder subproesses."""
        self.log_handler.log_info('Starting rtl_fm subprocess, listening on ' + \
            self.config.frequency() + '.')

        # Start rtl_fm subprocess which listens for APRS signals.
        rtl_subprocess = subprocess.Popen(
            ['rtl_fm', '-M', 'fm', '-f', self.config.frequency(), '-s',
            self.config.sample_rate(), '-l', '0', '-g', self.config.gain(), '-'],
            stdout=subprocess.PIPE, stderr=open('/dev/null')
        )

        self.sub_processes['rtl'] = rtl_subprocess

        self.log_handler.log_info('Starting multimon-ng subprocess.')

        # Start multimon-ng subprocess which decodes APRS data.
        multimon_subprocess = subprocess.Popen(
            ['multimon-ng', '-a', 'AFSK1200', '-A', '-t', 'raw', '-'],
            stdin=rtl_subprocess.stdout,
            stdout=subprocess.PIPE, stderr=open('/dev/null')
        )

        self.sub_processes['multimon'] = multimon_subprocess

    def __process_decoded_packet(self, decoded_packet):
        """Parses the decoded packet, logging the raw data to file
        and the user friendly, readavle data to console.

        Args:
            decoded_packet: The raw, decoded APRS packet string.
        """
        print_friendly_packet = \
            self.deserializer.to_readable_output(decoded_packet)
        self.log_handler.log_packet(decoded_packet, print_friendly_packet)

    def __clean_decoded_packet(self, decoded_packet):
        """Multimon-ng returns a string which starts with 'APRS: '.
        Naturally, this is not a valid part of an APRS packet, so that is
        stripped off.

        Multimon-ng also tends to output various debug info we don't care
        about in the slightest. So, we return None when that was received.

        Args:
            decoded_packet: The raw, decoded APRS packet string, uncleaned.
        """
        aprs_match = re.compile(r'^APRS: (.*)') \
            .match(decoded_packet)
        if aprs_match:
            return aprs_match.group(1)

        return None

    def __multimon_worker(self):
        """A worker thread handling output from the radio subprocess, sending
        the output to the Multimon-ng subprocess to decode.
        """
        self.log_handler.log_info('Worker thread starting.')

        while self.is_running:
            try:
                decoded_packet = self.sub_processes['multimon'] \
                    .stdout.readline().decode('utf-8').strip()

                cleaned_packet = self.__clean_decoded_packet(decoded_packet)

                if cleaned_packet is not None:
                    self.__process_decoded_packet(cleaned_packet)

            except UnicodeDecodeError:
                self.log_handler.log_warn('Unable to decode packet.')
