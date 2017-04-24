from pypacket.base.deserialization import Deserialization
from pypacket.util.colors import Colors

class TestDeserialization:
    def test_to_readable_output_nonsense_packet_expect_raw_returned(self):
        test_deserialization = Deserialization()
        expected_return = 'this is not a proper aprs packet'

        actual_value = test_deserialization.to_readable_output(expected_return)

        assert actual_value == expected_return

    def test_to_readable_output_reale_packet_expect_readable_returned(self):
        test_deserialization = Deserialization()
        test_packet = 'AAA123>BBB123,APRS-1*,WIDE1*,APRS-10*,WIDE2*:!4252.29NT07538.40W&PHG7130 Yes hello, testing.'
        expected_return = self.__get_prefix('from:') + 'AAA123' + \
            self.__get_prefix('to:') + 'BBB123' + \
            self.__get_prefix('format:') + 'uncompressed' + \
            self.__get_prefix('latitude:') + '42.8715' + \
            self.__get_prefix('longitude:') + '-75.64' + \
            self.__get_prefix('comment:') + 'Yes hello, testing.'

        actual_value = test_deserialization.to_readable_output(test_packet)

        assert actual_value == expected_return

    def __get_prefix(self, prefix):
        return '\r\n      ' + Colors.BOLD + prefix + Colors.RESET + ' '
