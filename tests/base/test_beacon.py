from pypacket.base.configuration import Configuration
from pypacket.framework.beacon import Beacon
from unittest.mock import patch


class TestBeacon:
    def test_beacon_expect_beacon(self):
        self.env = patch.dict('os.environ', {
            'PYPACKET_LATITUDE': '42',
            'PYPACKET_LONGITUDE': '-42'
        })

        with self.env:
            test_configuration = Configuration()

            beacon = Beacon(test_configuration)

            assert beacon.latitude == 42.0
            assert beacon.longitude == -42.0
