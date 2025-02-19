from abc import ABC, abstractmethod


class SubjectABC(ABC):

    @abstractmethod
    def register(self, observer):
        pass

    def unregister(self, observer):
        pass

    def notify(self, temp, humidity):
        pass
