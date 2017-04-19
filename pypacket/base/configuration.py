import json

class Configuration:
    CONFIG_FILE_NAME = 'config/configuration.json'

    def __init__(self):
        self.data = {}
        self.load()

    def load(self):
        with open(self.CONFIG_FILE_NAME) as json_data_file:
            self.data = json.load(json_data_file)

    def frequency(self):
        return self.data['rtl']['frequency']

    def gain(self):
        return self.data['rtl']['gain']

    def sample_rate(self):
        return self.data['rtl']['sample_rate']
