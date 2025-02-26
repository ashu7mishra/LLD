from abc import ABC, abstractmethod


class NonFlyable(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

    @abstractmethod
    def move(self):
        raise NotImplementedError