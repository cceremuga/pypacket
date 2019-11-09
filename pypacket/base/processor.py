from abc import ABC, abstractmethod


class ProcessorBase(ABC):
    @abstractmethod
    def load(self, config, log_handler):
        pass

    @abstractmethod
    def handle(self, packet):
        pass
