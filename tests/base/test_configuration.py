from pypacket.base.configuration import Configuration
from unittest.mock import patch


class TestConfiguration:
    def test_frequency_expect_frequency(self):
        test_configuration = Configuration()
        expected_frequency = '144390000'

        actual_frequency = test_configuration.frequency()

        assert actual_frequency == expected_frequency

    def test_sample_rate_expect_sample_rate(self):
        test_configuration = Configuration()
        expected_sample_rate = '22050'

        actual_sample_rate = test_configuration.sample_rate()

        assert actual_sample_rate == expected_sample_rate

    def test_gain_expect_gain(self):
        test_configuration = Configuration()
        expected_gain = '49.6'

        actual_gain = test_configuration.gain()

        assert actual_gain == expected_gain

    def test_listener_expect_listener(self):
        test_configuration = Configuration()

        actual_listener = test_configuration.listener()

        assert actual_listener is not None

    def test_decoder_expect_decoder(self):
        test_configuration = Configuration()

        actual_decoder = test_configuration.decoder()

        assert actual_decoder is not None

    def test_constructor_with_json_expect_constructed(self):
        mock_json = '{"listener":{"gain":"0"}}'
        test_configuration = Configuration()
        test_configuration.load_json(mock_json)

        actual_gain = test_configuration.gain()

        assert actual_gain == '0'

    def test_squelch_expect_squelch(self):
        mock_json = '{"listener":{"squelch_level":"5"}}'
        test_configuration = Configuration()
        test_configuration.load_json(mock_json)

        squelch_level = test_configuration.squelch_level()

        assert squelch_level == '5'

    def test_ppm_error_expect_ppm_error(self):
        mock_json = '{"listener":{"ppm_error":"5"}}'
        test_configuration = Configuration()
        test_configuration.load_json(mock_json)

        ppm_error = test_configuration.ppm_error()

        assert ppm_error == '5'

    def test_version_expect_version(self):
        mock_json = '{"version":4.5}'
        test_configuration = Configuration()
        test_configuration.load_json(mock_json)

        version = test_configuration.version()

        assert version == 4.5

    def test_beacon_interval_expect_beacon_interval(self):
        mock_json = '{"beacon":{"interval":30.0}}'
        test_configuration = Configuration()
        test_configuration.load_json(mock_json)

        beacon_interval = test_configuration.beacon_interval()

        assert beacon_interval == 30.0

    def test_beacon_comment_expect_beacon_comment(self):
        mock_json = '{"beacon":{"comment":"hello, world"}}'
        test_configuration = Configuration()
        test_configuration.load_json(mock_json)

        beacon_comment = test_configuration.beacon_comment()

        assert beacon_comment == "hello, world"

    def test_beacon_symbol_expect_beacon_symbol(self):
        mock_json = '{"beacon":{"symbol":"i"}}'
        test_configuration = Configuration()
        test_configuration.load_json(mock_json)

        beacon_symbol = test_configuration.beacon_symbol()

        assert beacon_symbol == "i"

    def test_beacon_symbol_table_expect_beacon_symbol_table(self):
        mock_json = '{"beacon":{"symbol_table":"/"}}'
        test_configuration = Configuration()
        test_configuration.load_json(mock_json)

        beacon_symbol_table = test_configuration.beacon_symbol_table()

        assert beacon_symbol_table == "/"

    def test_username_expect_username(self):
        self.env = patch.dict('os.environ', {'PYPACKET_USERNAME': 'test'})

        with self.env:
            test_configuration = Configuration()

            username = test_configuration.username()

            assert username == 'test'

    def test_password_expect_username(self):
        self.env = patch.dict('os.environ', {'PYPACKET_PASSWORD': 'supersecure'})

        with self.env:
            test_configuration = Configuration()

            password = test_configuration.password()

            assert password == 'supersecure'

    def test_latitude_expect_username(self):
        self.env = patch.dict('os.environ', {'PYPACKET_LATITUDE': '42'})

        with self.env:
            test_configuration = Configuration()

            latitude = test_configuration.latitude()

            assert latitude == '42'

    def test_longitude_expect_username(self):
        self.env = patch.dict('os.environ', {'PYPACKET_LONGITUDE': '-42'})

        with self.env:
            test_configuration = Configuration()

            longitude = test_configuration.longitude()

            assert longitude == '-42'
