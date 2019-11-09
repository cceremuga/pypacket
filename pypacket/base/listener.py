from abc import ABC, abstractmethod


class ListenerBase(ABC):
    @abstractmethod
    def load(self, config, log_handler):
        pass
