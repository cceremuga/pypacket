from pypacket.util.colors import Colors

class TestColors:
    def test_green_expect_green_value(self):
        expectedColor = '\033[92m'
        assert Colors.GREEN == expectedColor

    def test_yellow_expect_yellow_value(self):
        expectedColor = '\033[93m'
        assert Colors.YELLOW == expectedColor

    def test_red_expect_red_value(self):
        expectedColor = '\033[91m'
        assert Colors.RED == expectedColor

    def test_reset_expect_reset_value(self):
        expectedColor = '\033[0m'
        assert Colors.RESET == expectedColor

    def test_blue_expect_blue_value(self):
        expectedColor = '\033[94m'
        assert Colors.BLUE == expectedColor
