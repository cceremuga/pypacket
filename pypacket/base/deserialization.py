import aprslib

class Deserialization:
    """This handles deserialization of APRS packet data into a format which
    is much more easy to consume for humans.
    """

    def __init__(self):
        pass

    def to_readable_output(self, serialized_packet):
        try:
            packet = aprslib.parse(serialized_packet)
            return self.get_from(packet) + self.get_to(packet) + \
                self.get_lat(packet) + self.get_long(packet) + \
                self.get_text(packet) + self.get_comment(packet)
            #print(packet)
        except (aprslib.ParseError, aprslib.UnknownFormat) as exp:
            return serialized_packet

    def get_from(self, deserialized_packet):
        if 'from' not in deserialized_packet:
            return ''

        return '\033[;1mFrom:\033[0;0m ' + deserialized_packet['from']

    def get_to(self, deserialized_packet):
        if 'to' not in deserialized_packet:
            return ''

        return '\r\n      \033[;1mTo:\033[0;0m ' + deserialized_packet['to']

    def get_lat(self, deserialized_packet):
        if 'latitude' not in deserialized_packet:
            return ''

        return '\r\n      \033[;1mLat:\033[0;0m ' + str(deserialized_packet['latitude'])

    def get_long(self, deserialized_packet):
        if 'longitude' not in deserialized_packet:
            return ''

        return '\r\n      \033[;1mLong:\033[0;0m ' + str(deserialized_packet['longitude'])

    def get_text(self, deserialized_packet):
        if 'text' not in deserialized_packet:
            return ''

        return '\r\n      \033[;1mText:\033[0;0m ' + deserialized_packet['text']

    def get_comment(self, deserialized_packet):
        if 'comment' not in deserialized_packet:
            return ''

        return '\r\n      \033[;1mComment:\033[0;0m ' + deserialized_packet['comment']
