import pytest

from pypacket.base.receiver import Receiver
from pypacket.util.logger import Logger
from pypacket.base.configuration import Configuration


class TestReceiver:
    def test_init_expect_initialized(self):
        log_handler = Logger()
        runtime_configuration = Configuration()

        test_receiver = Receiver(log_handler, runtime_configuration)

        assert test_receiver.is_running is False
        assert test_receiver.sub_processes == {}
        assert test_receiver.log_handler == log_handler
        assert test_receiver.config == runtime_configuration

    def test_stop_expect_sys_exit(self):
        log_handler = Logger()
        runtime_configuration = Configuration()

        test_receiver = Receiver(log_handler, runtime_configuration)

        try:
            test_receiver.stop()
        except SystemExit:
            return

        pytest.fail('Expected a SystemExit to be raised.')

    def test_clean_decoded_packet_no_aprs_expect_none(self):
        log_handler = Logger()
        runtime_configuration = Configuration()
        mock_packet = 'blah'

        test_receiver = Receiver(log_handler, runtime_configuration)

        actual_packet = test_receiver._Receiver__clean_decoded_packet(mock_packet)

        assert actual_packet is None

    def test_clean_decoded_packet_with_aprs_expect_cleaned(self):
        log_handler = Logger()
        runtime_configuration = Configuration()
        expected_cleaned_packet = 'Woo'
        mock_packet = 'APRS: ' + expected_cleaned_packet

        test_receiver = Receiver(log_handler, runtime_configuration)

        actual_packet = test_receiver._Receiver__clean_decoded_packet(mock_packet)

        assert actual_packet == expected_cleaned_packet

    def test_start_with_mock_instances_expect_started(self):
        mock_json = '{"listener":{"implementation": "pypacket.mocks.mock_listener.MockListener"},' + \
            '"decoder":{"implementation": "pypacket.mocks.mock_decoder.MockDecoder"}, ' + \
            '"processors": [{"name": "mock", "implementation": "pypacket.mocks.mock_processor.MockProcessor"}]}'
        log_handler = Logger()
        runtime_configuration = Configuration()
        runtime_configuration.load_json(mock_json)

        test_receiver = Receiver(log_handler, runtime_configuration)

        test_receiver.start()

        assert test_receiver.is_running is True
