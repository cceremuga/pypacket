from abc import ABC, abstractmethod


class DecoderBase(ABC):
    @abstractmethod
    def load(self, config, log_handler, listener_subprocess):
        pass
