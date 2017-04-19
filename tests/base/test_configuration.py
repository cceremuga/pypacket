from pypacket.base.configuration import Configuration

class TestConfiguration:
    def test_frequency_expect_frequency(self, capsys):
        test_configuration = Configuration()
        expected_frequency = '144390000'

        actual_frequency = test_configuration.frequency()

        assert actual_frequency == expected_frequency

    def test_sample_rate_expect_sample_rate(self, capsys):
        test_configuration = Configuration()
        expected_sample_rate = '22050'

        actual_sample_rate = test_configuration.sample_rate()

        assert actual_sample_rate == expected_sample_rate

    def test_gain_expect_gain(self, capsys):
        test_configuration = Configuration()
        expected_gain = '49.6'

        actual_gain = test_configuration.gain()

        assert actual_gain == expected_gain
