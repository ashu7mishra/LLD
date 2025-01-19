from abc import ABC, abstractmethod

class User(ABC):

    @abstractmethod
    def signup(self):
        pass

    @abstractmethod
    def login(self):
        pass
