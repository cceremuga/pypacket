import abc


class ListenerBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self, config, log_handler):
        pass
