class Logger:
    def log_info(self, logMessage):
        print('[SYS] ' + logMessage)

    def log_error(self, logMessage):
        print('\033[91m[ERR] \033[0m' + logMessage)

    def log_warn(self, logMessage):
        print('\033[93m[WRN] \033[0m' + logMessage)

    def log_packet(self, logMessage):
        print('\033[92m[REC] \033[0m' + logMessage)
