import aprslib
from pypacket.util.colors import Colors

class Deserialization:
    """This handles deserialization of APRS packet data into a format which
    is much more easy to consume for humans.
    """

    SPACING_PREFIX = '\r\n      '

    def __init__(self):
        pass

    def to_readable_output(self, serialized_packet):
        try:
            packet = aprslib.parse(serialized_packet)
            return self.get_formatted(packet, 'from') + \
                self.get_formatted(packet, 'to') + \
                self.get_formatted(packet, 'latitude') + \
                self.get_formatted(packet, 'longitude') + \
                self.get_formatted(packet, 'comment') + \
                self.get_formatted(packet, 'text')
        except (aprslib.ParseError, aprslib.UnknownFormat) as exp:
            return serialized_packet

    def get_formatted(self, deserialized_packet, key):
        if key not in deserialized_packet:
            return ''

        return self.get_prefix(key + ':') + str(deserialized_packet[key])

    def get_prefix(self, prefix):
        return self.SPACING_PREFIX + Colors.BOLD + prefix + Colors.RESET + ' '
