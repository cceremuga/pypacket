import abc


class ProcessorBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self, config, log_handler, decoder_subprocess):
        pass
