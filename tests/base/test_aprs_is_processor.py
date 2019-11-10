from unittest import mock

from pypacket.base.aprs_is_processor import AprsIsProcessor
from pypacket.base.configuration import Configuration
from pypacket.util.logger import Logger

class TestAprsIsProcessor:
    @mock.patch('aprslib.IS.connect')
    def test_load_expect_connected(self, mock_connect):
        test_configuration = Configuration()
        test_logger = Logger()
        processor = AprsIsProcessor()

        processor.load(test_configuration, test_logger)

        mock_connect.assert_called_once()

    @mock.patch('aprslib.IS.sendall')
    def test_handle_expect_handled(self, mock_handle):
        test_configuration = Configuration()
        test_logger = Logger()
        processor = AprsIsProcessor()
        processor.is_connected = True
        processor.load(test_configuration, test_logger)

        processor.handle(None)

        mock_handle.assert_called_once()


