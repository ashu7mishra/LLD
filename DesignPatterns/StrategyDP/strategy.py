from abc import ABC, abstractmethod


class Sorting(ABC):
    @abstractmethod
    def sort(self):
        pass