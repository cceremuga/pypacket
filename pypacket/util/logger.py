import logging
import os
from time import localtime, strftime
from pypacket.util.colors import Colors

class Logger:
    SYS_PREFIX = '[SYS] '
    ERR_PREFIX = '[ERR] '
    WRN_PREFIX = '[WRN] '
    REC_PREFIX = '[REC] '
    LOG_DIRECTORY = 'logs'

    def __init__(self):
        self.setup()

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

    def setup(self):
        if not os.path.exists(self.LOG_DIRECTORY):
            os.makedirs(self.LOG_DIRECTORY)

        log_format = '[%(asctime)-15s] [%(levelname)s] %(message)s'
        log_file_name = self.LOG_DIRECTORY + '/pypacket_' + \
            strftime("%Y_%m_%d_%H_%M_%S", localtime()) + '.log'
        logging.basicConfig(filename=log_file_name, format=log_format, \
            level=logging.INFO)
