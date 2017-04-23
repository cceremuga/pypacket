from pypacket.util.colors import Colors

class TestColors:
    def test_green_expect_green_value(self):
        expected_color = '\033[92m'
        assert Colors.GREEN == expected_color

    def test_yellow_expect_yellow_value(self):
        expected_color = '\033[93m'
        assert Colors.YELLOW == expected_color

    def test_red_expect_red_value(self):
        expected_color = '\033[91m'
        assert Colors.RED == expected_color

    def test_reset_expect_reset_value(self):
        expected_color = '\033[0m'
        assert Colors.RESET == expected_color

    def test_blue_expect_blue_value(self):
        expected_color = '\033[94m'
        assert Colors.BLUE == expected_color

    def test_bold_expect_bold_value(self):
        expected_value = '\033[;1m'
        assert Colors.BOLD == expected_value
