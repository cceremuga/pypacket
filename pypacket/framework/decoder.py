from abc import ABC, abstractmethod


class Decoder(ABC):
    @abstractmethod
    def load(self, config, log_handler, listener_subprocess):
        pass
