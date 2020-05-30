from pypacket.framework.processor import Processor
from pypacket.base.deserialization import Deserialization


class CliProcessor(Processor):
    def __init__(self):
        """Sets up the functionality we will be using."""
        self.log_handler = None
        self.config = None
        self.deserializer = Deserialization()

    def get_name(self):
        """Gets the name of this processor to match against the config."""
        return "cli"

    def load(self, config, log_handler):
        """Initializes the processor, assigning the params locally..

        Args:
            packet: A decoded packet to output to the CLI.
        """
        self.config = config
        self.log_handler = log_handler

    def handle(self, packet):
        """Handles a single packet, outputting it to the CLI in a human-readable format.

        Args:
            packet: A decoded packet to output to the CLI.
        """
        print_friendly_packet = self.deserializer.to_readable_output(packet)
        self.log_handler.log_packet(packet, print_friendly_packet)
