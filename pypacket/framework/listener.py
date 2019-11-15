from abc import ABC, abstractmethod


class Listener(ABC):
    @abstractmethod
    def load(self, config, log_handler):
        pass
