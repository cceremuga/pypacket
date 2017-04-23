import logging
import os
from time import localtime, strftime
from pypacket.util.colors import Colors

class Logger:
    """A utility logger class for purposes of logging things to console as
    well as to file via the Python logging utility.
    """

    SYS_PREFIX = '[SYS] '
    ERR_PREFIX = '[ERR] '
    WRN_PREFIX = '[WRN] '
    REC_PREFIX = '[REC] '
    LOG_DIRECTORY = 'logs'

    def __init__(self):
        """Sets up the logger, via calling setup()."""
        self.setup()

    def log_info(self, logMessage):
        """Logs an info message to console, file.

        Args:
            logMessage: The string message to log.
        """
        self.log_any(Colors.BLUE, self.SYS_PREFIX, logMessage)
        logging.info(logMessage)

    def log_error(self, logMessage):
        """Logs an error message to console, file.

        Args:
            logMessage: The string message to log.
        """
        self.log_any(Colors.RED, self.ERR_PREFIX, logMessage)
        logging.error(logMessage)

    def log_warn(self, logMessage):
        """Logs a warning message to console, file.

        Args:
            logMessage: The string message to log.
        """
        self.log_any(Colors.YELLOW, self.WRN_PREFIX, logMessage)
        logging.warning(logMessage)

    def log_packet(self, rawMessage, friendlyMessage):
        """Logs a raw packet message to file, friendly to console.
        Intended to log raw, decoded APRS packets to file with a user-readable
        version to the CLI.

        Args:
            rawMessage: The raw string message to log to file.
            friendlyMessage: The user friendly message to log to CLI.
        """
        self.log_any(Colors.GREEN, self.REC_PREFIX, friendlyMessage)
        logging.info(rawMessage)

    def log_any(self, color, prefix, logMessage):
        """Logs any message to system console.

        Args:
            color: The color escape sequence to use.
            prefix: A string prefix such as [INFO].
            logMessage: The string message to log.
        """
        print(color + prefix + Colors.RESET + logMessage)

    def setup(self):
        """Sets up the logger. First checks to see if the log directory exists.
        If the directory does not exist, it creates it.

        Then, configures the Python logger with our chosen format and a file
        name based upon the date / time when the logger instance is initialized.
        """
        if not os.path.exists(self.LOG_DIRECTORY):
            os.makedirs(self.LOG_DIRECTORY)

        log_format = '[%(asctime)-15s] [%(levelname)s] %(message)s'
        log_file_name = self.LOG_DIRECTORY + '/pypacket_' + \
            strftime("%Y_%m_%d_%H_%M_%S", localtime()) + '.log'
        logging.basicConfig(filename=log_file_name, format=log_format, \
            level=logging.INFO)
