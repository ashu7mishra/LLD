from abc import ABC, abstractmethod


class Ink(ABC):

    def __init__(self, color: str, density: float):

        self._color = color
        self._density = density

    @abstractmethod
    def set_color(self, color: str):
        raise NotImplementedError

    @abstractmethod
    def set_density(self, density: str):
        raise NotImplementedError

    @abstractmethod
    def get_color(self):
        raise NotImplementedError

    @abstractmethod
    def get_density(self):
        raise NotImplementedError

