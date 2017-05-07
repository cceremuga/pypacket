import subprocess
import mock
from pypacket.base.receiver import Receiver
from pypacket.util.logger import Logger
from pypacket.base.deserialization import Deserialization
from pypacket.base.configuration import Configuration

class TestReceiver:
    def test_init_expect_initialized(self):
        log_handler = Logger()
        runtime_configuration = Configuration()
        deserializer = Deserialization()

        test_receiver = \
            Receiver(log_handler, deserializer, runtime_configuration)

        assert test_receiver.is_running == False
        assert test_receiver.subprocesses == {}
        assert test_receiver.log_handler == log_handler
        assert test_receiver.deserializer == deserializer
        assert test_receiver.config == runtime_configuration

    def test_stop_expect_sys_exit(self):
        log_handler = Logger()
        runtime_configuration = Configuration()
        deserializer = Deserialization()

        test_receiver = \
            Receiver(log_handler, deserializer, runtime_configuration)

        try:
            test_receiver.stop()
        except SystemExit:
            return

        pytest.fail('Expected a SystemExit to be raised.')

    def test_clean_decoded_packet_no_aprs_expect_none(self):
        log_handler = Logger()
        runtime_configuration = Configuration()
        deserializer = Deserialization()
        mock_packet = 'blah'

        test_receiver = \
            Receiver(log_handler, deserializer, runtime_configuration)

        actual_packet = \
            test_receiver._Receiver__clean_decoded_packet(mock_packet)

        assert actual_packet == None

    def test_clean_decoded_packet_with_aprs_expect_cleaned(self):
        log_handler = Logger()
        runtime_configuration = Configuration()
        deserializer = Deserialization()
        expected_cleaned_packet = 'Woo'
        mock_packet = 'APRS: ' + expected_cleaned_packet

        test_receiver = \
            Receiver(log_handler, deserializer, runtime_configuration)

        actual_packet = \
            test_receiver._Receiver__clean_decoded_packet(mock_packet)

        assert actual_packet == expected_cleaned_packet

    def test_start_with_mock_instances_expect_started(self):
        mock_json = '{"listener":{"module": "pypacket.base.mock_listener",' + \
            '"class": "MockListener"},"decoder":{"module": ' + \
            '"pypacket.base.mock_decoder","class": "MockDecoder"}}'
        log_handler = Logger()
        runtime_configuration = Configuration()
        runtime_configuration.load_json(mock_json)
        deserializer = Deserialization()

        test_receiver = \
            Receiver(log_handler, deserializer, runtime_configuration)

        test_receiver.start()

        assert test_receiver.is_running == True
