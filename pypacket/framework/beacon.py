from aprslib.packets.position import PositionReport


class Beacon(PositionReport):
    def __init__(self, config):
        """Constructs a telemtry beacon for the IGate with the specified latitude, longitude."""
        self.fromcall = config.username()
        self.tocall = 'APRS'
        self.latitude = float(config.latitude())
        self.longitude = float(config.longitude())
        self.comment = '{0} https://pypacket.app v{1}'.format(config.beacon_comment(), config.version())
        self.symbol = config.beacon_symbol()
        self.symbol_table = config.beacon_symbol_table()
