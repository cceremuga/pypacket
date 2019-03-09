from pypacket.util.logger import Logger
from pypacket.util.colors import Colors


class TestLogger:
    PRINT_SUFFIX = '\n'

    def test_log_info_expect_logged(self, capsys):
        mock_info = 'Hey, check out this info.'
        expected_info = Colors.BLUE + Logger.SYS_PREFIX + Colors.RESET + \
            mock_info + self.PRINT_SUFFIX

        Logger().log_info(mock_info)

        out, err = capsys.readouterr()
        assert out == expected_info

    def test_log_error_expect_logged(self, capsys):
        mock_error = 'Hey, check out this error.'
        expected_error = Colors.RED + Logger.ERR_PREFIX + Colors.RESET + \
            mock_error + self.PRINT_SUFFIX

        Logger().log_error(mock_error)

        out, err = capsys.readouterr()
        assert out == expected_error

    def test_log_warn_expect_logged(self, capsys):
        mock_warn = 'Hey, check out this warning.'
        expected_warn = Colors.YELLOW + Logger.WRN_PREFIX + Colors.RESET + \
            mock_warn + self.PRINT_SUFFIX

        Logger().log_warn(mock_warn)

        out, err = capsys.readouterr()
        assert out == expected_warn

    def test_log_packet_expect_logged(self, capsys):
        mock_packet = 'Hey, check out this packet.'
        expected_packet = Colors.GREEN + Logger.REC_PREFIX + Colors.RESET + \
            mock_packet + self.PRINT_SUFFIX

        Logger().log_packet(mock_packet, mock_packet)

        out, err = capsys.readouterr()
        assert out == expected_packet
