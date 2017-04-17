import logging
from pypacket.util.colors import Colors

class Logger:
    SYS_PREFIX = '[SYS] '
    ERR_PREFIX = '[ERR] '
    WRN_PREFIX = '[WRN] '
    REC_PREFIX = '[REC] '

    def log_info(self, logMessage):
        self.log_any(Colors.BLUE, self.SYS_PREFIX, logMessage)
        logging.info(logMessage)

    def log_error(self, logMessage):
        self.log_any(Colors.RED, self.ERR_PREFIX, logMessage)
        logging.error(logMessage)

    def log_warn(self, logMessage):
        self.log_any(Colors.YELLOW, self.WRN_PREFIX, logMessage)
        logging.warning(logMessage)

    def log_packet(self, logMessage):
        self.log_any(Colors.GREEN, self.REC_PREFIX, logMessage)
        logging.info(logMessage)

    def log_any(self, color, prefix, logMessage):
        print(color + prefix + Colors.RESET + logMessage)
