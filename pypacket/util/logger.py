from pypacket.util.colors import Colors

class Logger:
    SYS_PREFIX = '[SYS] '
    ERR_PREFIX = '[ERR] '
    WRN_PREFIX = '[WRN] '
    REC_PREFIX = '[REC] '

    def log_info(self, logMessage):
        print(self.SYS_PREFIX + logMessage)

    def log_error(self, logMessage):
        print(Colors.RED + self.ERR_PREFIX + Colors.RESET + logMessage)

    def log_warn(self, logMessage):
        print(Colors.YELLOW + self.WRN_PREFIX + Colors.RESET + logMessage)

    def log_packet(self, logMessage):
        print(Colors.GREEN + self.REC_PREFIX + Colors.RESET + logMessage)
