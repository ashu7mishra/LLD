from abc import ABC, abstractmethod


class Flyable(ABC):

    @abstractmethod
    def fly(self):
        raise NotImplementedError

    @abstractmethod
    def move(self):
        raise NotImplementedError
