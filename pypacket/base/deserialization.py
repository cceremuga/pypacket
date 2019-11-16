import aprslib
import re

from pypacket.util.colors import Colors
from terminaltables import SingleTable


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

            table_data = [
                [
                    "From     ",
                    "To       ",
                    "Lat     ",
                    "Long    ",
                    "Comment                    ",
                    "Text                       "
                ], [
                    self.__get_formatted(packet, 'from', 9),
                    self.__get_formatted(packet, 'to', 9),
                    self.__get_formatted(packet, 'latitude', 8),
                    self.__get_formatted(packet, 'longitude', 8),
                    self.__get_formatted(packet, 'comment', 27),
                    self.__get_formatted(packet, 'text', 27),
                ]
            ]
            table_instance = SingleTable(table_data, ' Packet ')
            table_instance.inner_heading_row_border = False
            table_instance.inner_row_border = True
            return table_instance.table
        except (aprslib.ParseError, aprslib.UnknownFormat):
            return serialized_packet

    def __get_formatted(self, deserialized_packet, key, split):
        if key not in deserialized_packet:
            return ''

        packet_field_value = str(deserialized_packet[key])
        return re.sub("(.{" + str(split) + "})", "\\1\n", packet_field_value, 0, re.DOTALL)
