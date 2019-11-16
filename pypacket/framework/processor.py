from abc import ABC, abstractmethod


class Processor(ABC):
    @abstractmethod
    def load(self, config, log_handler):
        pass

    @abstractmethod
    def handle(self, packet):
        pass

    @abstractmethod
    def get_name(self):
        pass
