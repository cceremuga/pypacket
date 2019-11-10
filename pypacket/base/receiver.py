import threading
import re
import sys


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

    def __init__(self, log_handler, deserializer, config):
        """Initializes the instance of Listener and starts listening."""
        self.is_running = False
        self.sub_processes = {}
        self.log_handler = log_handler
        self.deserializer = deserializer
        self.config = config
        self.worker_thread = None
        self.processor = None

    def start(self):
        """Starts the listener, decoder sub-processes, processor. Starts a worker thread."""
        listener = self.config.listener()
        self.sub_processes['listener'] = listener.load(self.config, self.log_handler)

        decoder = self.config.decoder()
        self.sub_processes['decoder'] = decoder.load(self.config, self.log_handler, self.sub_processes['listener'])

        self.processor = self.config.processor()
        self.processor.load(self.config, self.log_handler)

        # Throw the sub-processes into a worker thread.
        self.is_running = True
        self.worker_thread = threading.Thread(target=self.__decoder_worker)
        self.worker_thread.setDaemon(True)
        self.worker_thread.start()

    def stop(self):
        """Stops all sub-processes, performs a system exit."""
        for key in self.sub_processes:
            self.sub_processes[key].terminate()

        self.log_handler.log_info('Interrupt received, exiting.')

        sys.exit(0)

    def __process_decoded_packet(self, decoded_packet):
        """Parses the decoded packet, logging the raw data to file
        and the user friendly, readable data to console. Passes along
        to the configured processor.

        Args:
            decoded_packet: The raw, decoded APRS packet string.
        """
        print_friendly_packet = self.deserializer.to_readable_output(decoded_packet)
        self.log_handler.log_packet(decoded_packet, print_friendly_packet)
        self.processor.handle(decoded_packet)

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
        self.log_handler.log_info('Worker thread starting.')

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
