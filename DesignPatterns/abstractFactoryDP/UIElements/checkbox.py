from abc import ABC, abstractmethod


class CheckBox(ABC):

    @abstractmethod
    def click(self):
        pass