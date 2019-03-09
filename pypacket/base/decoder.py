import abc


class DecoderBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self, config, log_handler, listener_subprocess):
        pass
