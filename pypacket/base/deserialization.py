import aprslib
from pypacket.util.colors import Colors


class Deserialization:
    """This handles deserialization of APRS packet data into a format which
    is much more easy to consume for humans.
    """

    SPACING_PREFIX = '\r\n      '

    def __init__(self):
        """Does nothing at this time."""
        pass

    def to_readable_output(self, serialized_packet):
        """Converts the decoded, but serialized packet to a clean, readable
        output. Intended for human readability.

        Args:
            serialized_packet: The raw, decoded APRS packet string.
        """
        try:
            packet = aprslib.parse(serialized_packet)
            return self.__get_formatted(packet, 'from').replace(self.SPACING_PREFIX, '') + \
                self.__get_formatted(packet, 'to') + \
                self.__get_formatted(packet, 'format') + \
                self.__get_formatted(packet, 'latitude') + \
                self.__get_formatted(packet, 'longitude') + \
                self.__get_formatted(packet, 'altitude') + \
                self.__get_formatted(packet, 'comment') + \
                self.__get_formatted(packet, 'text')
        except (aprslib.ParseError, aprslib.UnknownFormat) as exp:
            return serialized_packet

    def __get_formatted(self, deserialized_packet, key):
        if key not in deserialized_packet:
            return ''

        return self.__get_prefix(key + ':') + str(deserialized_packet[key])

    def __get_prefix(self, prefix):
        return self.SPACING_PREFIX + Colors.BOLD + prefix + Colors.RESET + ' '
