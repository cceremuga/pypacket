import json
import importlib
import os


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

    def version(self):
        """Gets the PyPacket version."""
        return self.data['version']

    def beacon_interval(self):
        """Gets the beacon interval."""
        return self.data['beacon']['interval']

    def beacon_comment(self):
        """Gets the beacon comment."""
        return self.data['beacon']['comment']

    def beacon_symbol(self):
        """Gets the beacon symbol."""
        return self.data['beacon']['symbol']

    def beacon_symbol_table(self):
        """Gets the beacon symbol table."""
        return self.data['beacon']['symbol_table']

    def username(self):
        """Gets the APRS-IS username (callsign)."""
        return os.environ.get('PYPACKET_USERNAME')

    def password(self):
        """Gets the APRS-IS password."""
        return os.environ.get('PYPACKET_PASSWORD')

    def latitude(self):
        """Gets the beacon latitude."""
        return os.environ.get('PYPACKET_LATITUDE')

    def longitude(self):
        """Gets the beacon longitude"""
        return os.environ.get('PYPACKET_LONGITUDE')

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
        """Loads in JSON config, assigning to data."""
        with open(self.CONFIG_FILE_NAME) as json_data_file:
            self.data = json.load(json_data_file)
