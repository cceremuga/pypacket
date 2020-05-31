import threading
import re
import sys
from subprocess import TimeoutExpired
from collections import OrderedDict


class Receiver:
    """This is the main receiver class for PyPacket. It spawns two sub-processes
    in a separate thread.

    The first sub-process is the listener which listens on the configured
    frequency, sending all raw output to the second sub-process.

    The second sub-process is the decoder process. Once a received packet
    has been decoded, it is cleaned up, leaving the raw APRS String.

    The string is then logged to file and output to the CLI for easy reading.

    Portions of this source code are inspired by architectural concepts found
    in the PyMultimonAPRS project (https://github.com/asdil12/pymultimonaprs).

    Attributes:
        config: The instance of Configuration containing all runtime options.
        log_handler: The instance of Logger containing all logging operations.
        sub-processes: A collection of sub-processes, initialized in start().
        is_running: Indicates whether or not the listener is running.
        worker_thread: A separate thread handling all sub-processes.
    """

    def __init__(self, log_handler, config):
        """Initializes the instance of Listener and starts listening."""
        self.is_running = False
        self.sub_processes = OrderedDict({})
        self.log_handler = log_handler
        self.config = config
        self.worker_thread = None
        self.processors = None

    def start(self):
        """Starts the listener, decoder sub-processes, processors. Starts a worker thread."""
        listener = self.__get_listener()
        self.sub_processes['listener'] = listener
        self.sub_processes['decoder'] = self.__get_decoder(listener)

        self.processors = self.config.processors()
        for processor in self.processors:
            # Load each processor.
            processor.load(self.config, self.log_handler)

        # Throw the sub-processes into a worker thread.
        self.is_running = True
        self.worker_thread = threading.Thread(target=self.__decoder_worker)
        self.worker_thread.setDaemon(True)
        self.worker_thread.start()

    def stop(self):
        """Kills all sub-processes inside-out, performs a system exit."""
        self.log_handler.log_info('Interrupt received, exiting.')

        if self.sub_processes:
            for key in reversed(self.sub_processes):
                self.sub_processes[key].kill()

        sys.exit(0)

    def __get_decoder(self, listener):
        """Gets the decoder subprocess from the config."""
        decoder = self.config.decoder()
        return decoder.load(self.config, self.log_handler, listener)

    def __get_listener(self):
        """Gets the listener subprocess from the config."""
        listener = self.config.listener()
        listener_subprocess = listener.load(self.config, self.log_handler)

        exit_code = 0

        try:
            # It will exit immediately with a 1 if there is a listener subprocess crash.
            exit_code = listener_subprocess.wait(5)
        except TimeoutExpired:
            # If the timeout has expired after 5 seconds, the listener is working just fine.
            exit_code = 0

        if exit_code == 1:
            self.log_handler.log_error('Listener subprocess did not start successfully.')
            sys.exit(1)

        return listener_subprocess

    def __process_decoded_packet(self, decoded_packet):
        """Parses the decoded packet, logging the raw data to file
        and the user friendly, readable data to console. Passes along
        to the configured processor.

        Args:
            decoded_packet: The raw, decoded APRS packet string.
        """
        for processor in self.processors:
            # Process in all configured processors.
            processor.handle(decoded_packet)

    def __clean_decoded_packet(self, decoded_packet):
        """Multimon-ng returns a string which starts with 'APRS: '.
        Naturally, this is not a valid part of an APRS packet, so that is
        stripped off.

        Multimon-ng also tends to output various debug info we don't care
        about in the slightest. So, we return None when that was received.

        Args:
            decoded_packet: The raw, decoded APRS packet string, uncleaned.
        """
        aprs_match = re.compile(r'^APRS: (.*)').match(decoded_packet)
        if aprs_match:
            return aprs_match.group(1)

        return None

    def __decoder_worker(self):
        """A worker thread handling output from the decoder sub-process."""
        self.log_handler.log_info('Worker thread started.')

        while self.is_running:
            try:
                decoder = self.sub_processes['decoder']

                if decoder is None or decoder.stdout is None:
                    continue

                decoded_packet = decoder.stdout.readline().decode('utf-8').strip()
                cleaned_packet = self.__clean_decoded_packet(decoded_packet)

                if cleaned_packet is not None:
                    self.__process_decoded_packet(cleaned_packet)

            except UnicodeDecodeError:
                self.log_handler.log_warn('Unable to decode packet.')
