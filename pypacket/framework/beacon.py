from aprslib.packets.position import PositionReport


class Beacon(PositionReport):
    def __init__(self, config):
        """Constructs a telemtry beacon for the IGate with the specified latitude, longitude."""
        self.fromcall = config.username()
        self.tocall = 'APRS'
        self.latitude = float(config.latitude())
        self.longitude = float(config.longitude())
        self.comment = 'PyPacket IGate v{0}'.format(config.version())
        self.symbol = 'I'
