from pypacket.base.configuration import Configuration
from pypacket.framework.beacon import Beacon
from unittest.mock import patch


class TestBeacon:
    def test_beacon_expect_beacon(self):
        mock_json = '{"version":"5.0","beacon":{"interval": 10.0,"comment": "Powered by","symbol_table": "I","symbol": "&"},"processors":[{"name":"test","position_precision":0}]}'
        self.env = patch.dict('os.environ', {
            'PYPACKET_LATITUDE': '42',
            'PYPACKET_LONGITUDE': '-42'
        })

        with self.env:
            test_configuration = Configuration()
            test_configuration.load_json(mock_json)

            beacon = Beacon(test_configuration, 'test')

            assert beacon.latitude == 42.0
            assert beacon.longitude == -42.0
