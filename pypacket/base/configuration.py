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

    def squelch_level(self):
        """Gets the configured squelch level."""
        return self.data['listener']['squelch_level']

    def ppm_error(self):
        """Gets the configured ppm error."""
        return self.data['listener']['ppm_error']

    def listener(self):
        """Gets the configured, instantiated listener class."""
        module_class_name = self.data['listener']['implementation'].rpartition('.')
        module = importlib.import_module(module_class_name[0])
        class_ = getattr(module, module_class_name[2])
        return class_()

    def decoder(self):
        """Gets the configured, instantiated decoder class."""
        module_class_name = self.data['decoder']['implementation'].rpartition('.')
        module = importlib.import_module(module_class_name[0])
        class_ = getattr(module, module_class_name[2])
        return class_()

    def processors(self):
        """Gets the configured, instantiated processor classes."""
        processors = []

        for processor in self.data['processors']:
            module_class_name = processor['implementation'].rpartition('.')
            module = importlib.import_module(module_class_name[0])
            class_ = getattr(module, module_class_name[2])
            processors.append(class_())

        return processors

    def host(self, name):
        """Gets the configured processor host."""
        for processor in self.data['processors']:
            if processor['name'] == name:
                return processor['host']

        return ''

    def load_json(self, json_data):
        """Loads in JSON data from a String, assigning to data."""
        self.data = json.loads(json_data)

    def __load(self):
        """Loads in JSON data from the config file, assigning to data."""
        with open(self.CONFIG_FILE_NAME) as json_data_file:
            self.data = json.load(json_data_file)
