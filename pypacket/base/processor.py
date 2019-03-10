import abc


class ProcessorBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self, config, log_handler):
        pass

    @abc.abstractmethod
    def handle(self, packet):
        pass
