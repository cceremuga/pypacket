from pypacket.util.colors import Colors

class Logger:
    def log_info(self, logMessage):
        print('[SYS] ' + logMessage)

    def log_error(self, logMessage):
        print(Colors.RED + '[ERR] ' + Colors.RESET + logMessage)

    def log_warn(self, logMessage):
        print(Colors.YELLOW + '[WRN] ' + Colors.RESET + logMessage)

    def log_packet(self, logMessage):
        print(Colors.GREEN + '[REC] ' + Colors.RESET + logMessage)
