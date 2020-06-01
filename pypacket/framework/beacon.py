from aprslib.packets.position import PositionReport


class Beacon(PositionReport):
    def __init__(self, config, processor_name):
        """Constructs a telemtry beacon for the IGate with the specified latitude, longitude."""
        self.fromcall = config.username()
        self.tocall = 'APRS'
        self.latitude = float(config.latitude(processor_name))
        self.longitude = float(config.longitude(processor_name))
        self.comment = '{0} https://pypacket.app v{1}'.format(config.beacon_comment(), config.version())
        self.symbol = config.beacon_symbol()
        self.symbol_table = config.beacon_symbol_table()
