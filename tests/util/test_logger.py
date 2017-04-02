from pypacket.util.logger import Logger
from pypacket.util.colors import Colors

class TestLogger:
    PRINT_SUFFIX = '\n'

    def test_log_info_expect_logged(self, capsys):
        mockInfo = 'Hey, check out this info.'
        expectedInfo = Colors.BLUE + Logger.SYS_PREFIX + Colors.RESET + \
            mockInfo + self.PRINT_SUFFIX

        Logger().log_info(mockInfo)

        out, err = capsys.readouterr()
        assert out == expectedInfo

    def test_log_error_expect_logged(self, capsys):
        mockError = 'Hey, check out this error.'
        expectedError = Colors.RED + Logger.ERR_PREFIX + Colors.RESET + \
            mockError + self.PRINT_SUFFIX

        Logger().log_error(mockError)

        out, err = capsys.readouterr()
        assert out == expectedError

    def test_log_warn_expect_logged(self, capsys):
        mockWarn = 'Hey, check out this warning.'
        expectedWarn = Colors.YELLOW + Logger.WRN_PREFIX + Colors.RESET + \
            mockWarn + self.PRINT_SUFFIX

        Logger().log_warn(mockWarn)

        out, err = capsys.readouterr()
        assert out == expectedWarn

    def test_log_packet_expect_logged(self, capsys):
        mockPacket = 'Hey, check out this packet.'
        expectedPacket = Colors.GREEN + Logger.REC_PREFIX + Colors.RESET + \
            mockPacket + self.PRINT_SUFFIX

        Logger().log_packet(mockPacket)

        out, err = capsys.readouterr()
        assert out == expectedPacket
