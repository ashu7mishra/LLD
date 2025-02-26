from abc import ABC, abstractmethod


class Bird(ABC):

    def __init__(self, name, color, height, weight, wings):
        self._name = name
        self._color = color
        self._height = height
        self._weight = weight
        self._wings = wings

    @abstractmethod
    def eat(self):
        raise NotImplementedError

    @abstractmethod
    def make_sound(self):
        raise NotImplementedError

    @abstractmethod
    def set_name(self, name):
        raise NotImplementedError

    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abstractmethod
    def set_color(self, color):
        raise NotImplementedError

    @abstractmethod
    def get_color(self):
        raise NotImplementedError

    @abstractmethod
    def set_height(self, height):
        raise NotImplementedError

    @abstractmethod
    def get_height(self):
        raise NotImplementedError

    @abstractmethod
    def set_weight(self, weight):
        raise NotImplementedError

    @abstractmethod
    def get_weight(self):
        raise NotImplementedError

    @abstractmethod
    def set_wings(self, name):
        raise NotImplementedError

    @abstractmethod
    def get_wings(self):
        raise NotImplementedError

