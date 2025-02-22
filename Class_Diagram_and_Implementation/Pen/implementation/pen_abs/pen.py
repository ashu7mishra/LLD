from abc import ABC, abstractmethod


class Pen(ABC):

    def __init__(self, pen_type: str, name: str, brand: str, price: int):
        self._pen_type = pen_type
        self._name = name
        self._brand = brand
        self._price = price
        self._closingType = None

    @abstractmethod
    def write(self):
        raise NotImplementedError

    @abstractmethod
    def open_close(self):
        raise NotImplementedError

    @abstractmethod
    def set_name(self, name):
        raise NotImplementedError

    @abstractmethod
    def set_type(self, pen_type):
        raise NotImplementedError

    @abstractmethod
    def set_brand(self, brand):
        raise NotImplementedError

    @abstractmethod
    def set_price(self, price):
        raise NotImplementedError

    @abstractmethod
    def set_closing_type(self, closing_type):
        raise NotImplementedError

    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abstractmethod
    def get_type(self):
        raise NotImplementedError

    @abstractmethod
    def get_brand(self):
        raise NotImplementedError

    @abstractmethod
    def get_price(self):
        raise NotImplementedError

    @abstractmethod
    def get_closing_type(self):
        raise NotImplementedError
