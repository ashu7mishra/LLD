from abc import ABC, abstractmethod


class ObserverABC(ABC):

    @abstractmethod
    def register(self, subject):
        pass

    @abstractmethod
    def unregister(self, subject):
        pass