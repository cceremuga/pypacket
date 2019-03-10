import json
import importlib


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
        self.__load()

    def frequency(self):
        """Gets the configured listener frequency setting."""
        return self.data['listener']['frequency']

    def gain(self):
        """Gets the configured listener gain setting."""
        return self.data['listener']['gain']

    def sample_rate(self):
        """Gets the configured listener sample rate setting."""
        return self.data['listener']['sample_rate']

    def listener(self):
        """Gets the configured, instantiated listener class."""
        module = importlib.import_module(self.data['listener']['module'])
        class_ = getattr(module, self.data['listener']['class'])
        return class_()

    def decoder(self):
        """Gets the configured, instantiated decoder class."""
        module = importlib.import_module(self.data['decoder']['module'])
        class_ = getattr(module, self.data['decoder']['class'])
        return class_()

    def processor(self):
        """Gets the configured, instantiated processor class."""
        module = importlib.import_module(self.data['processor']['module'])
        class_ = getattr(module, self.data['processor']['class'])
        return class_()

    def how_often_to_process(self):
        """Gets the configured processor how_often_to_process."""
        return self.data['processor']['how_often_to_process']

    def host(self):
        """Gets the configured processor host."""
        return self.data['processor']['host']

    def load_json(self, json_data):
        """Loads in JSON data from a String, assigning to data."""
        self.data = json.loads(json_data)

    def __load(self):
        """Loads in JSON data from the config file, assigning to data."""
        with open(self.CONFIG_FILE_NAME) as json_data_file:
            self.data = json.load(json_data_file)
