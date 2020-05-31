from os import environ
from unittest import mock

from pypacket.base.configuration import Configuration
from pypacket.implementations.aprs_is_processor import AprsIsProcessor
from pypacket.util.logger import Logger


class TestAprsIsProcessor:
    @mock.patch('aprslib.IS.connect')
    def test_load_env_vars_not_set_expect_not_connected(self, mock_connect):
        test_configuration = Configuration()
        test_logger = Logger()
        processor = AprsIsProcessor()

        processor.load(test_configuration, test_logger)

        mock_connect.assert_not_called()

    @mock.patch('aprslib.IS.connect')
    def test_load_expect_connected(self, mock_connect):
        environ['PYPACKET_USERNAME'] = 'test'
        environ['PYPACKET_PASSWORD'] = 'test'

        test_configuration = Configuration()
        test_logger = Logger()
        processor = AprsIsProcessor()

        processor.load(test_configuration, test_logger)

        mock_connect.assert_called_once()

    @mock.patch('aprslib.IS.sendall')
    def test_handle_expect_handled(self, mock_handle):
        environ['PYPACKET_USERNAME'] = 'test'
        environ['PYPACKET_PASSWORD'] = 'test'

        test_configuration = Configuration()
        test_logger = Logger()
        processor = AprsIsProcessor()
        processor.is_connected = True
        processor.load(test_configuration, test_logger)

        processor.handle(None)

        mock_handle.assert_called_once()
