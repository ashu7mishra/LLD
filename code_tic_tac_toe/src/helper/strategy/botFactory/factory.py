from abc import ABC, abstractmethod

class Factory(ABC):

    @abstractmethod
    def getBot(self):
        raise NotImplementedError