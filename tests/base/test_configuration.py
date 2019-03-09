from pypacket.base.configuration import Configuration


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
