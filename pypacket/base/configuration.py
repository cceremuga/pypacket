import json

class Configuration:
    """Loads in JSON configuration from file, providing various methods to
    access individual configuration data pieces.

    Attributes:
        data: The dictionary which is loaded with deserialized JSON at load().
    """

    CONFIG_FILE_NAME = 'config/configuration.json'

    def __init__(self):
        """Initializes the instance of Configuration, loading in JSON data."""
        self.data = {}
        self.load()

    def load(self):
        """Loads in JSON data from the config file, assigning to data."""
        with open(self.CONFIG_FILE_NAME) as json_data_file:
            self.data = json.load(json_data_file)

    def frequency(self):
        """Gets the configured RTL frequency setting."""
        return self.data['rtl']['frequency']

    def gain(self):
        """Gets the configured RTL gain setting."""
        return self.data['rtl']['gain']

    def sample_rate(self):
        """Gets the configured RTL sample rate setting."""
        return self.data['rtl']['sample_rate']
