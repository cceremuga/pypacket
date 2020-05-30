from pypacket.base.configuration import Configuration
from pypacket.util.logger import Logger
from pypacket.framework.beacon import Beacon
from pypacket.implementations.cli_processor import CliProcessor


class TestCliProcessor:
    def test_get_name_expect_cli(self):
        cli_processor = CliProcessor()

        name = cli_processor.get_name()

        assert name == 'cli'

    def test_load_expect_loaded(self):
        test_logger = Logger()
        test_configuration = Configuration()
        cli_processor = CliProcessor()

        cli_processor.load(test_configuration, test_logger)

        assert cli_processor.config == test_configuration
        assert cli_processor.log_handler == test_logger

    def test_handler_expect_handled_without_error(self):
        mock_packet = 'AAA123>BBB123,APRS-1*,WIDE1*,APRS-10*,WIDE2*:!4252.29NT07538.40W&PHG7130 Yes hello, testing.'
        test_logger = Logger()
        test_configuration = Configuration()
        cli_processor = CliProcessor()
        cli_processor.load(test_configuration, test_logger)

        cli_processor.handle(mock_packet)
