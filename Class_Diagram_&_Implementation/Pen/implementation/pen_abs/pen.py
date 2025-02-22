from abc import ABC, abstractmethod
from closingType import ClosingType


class Pen(ABC):

    def __init__(self, type: str, name: str, brand: str, price: int):
        self.name = name
        self.type = type
        self.brand = brand
        self.price = price
        self.closing = ClosingType()

    @abstractmethod
    def write(self):
        raise NotImplementedError

    @abstractmethod
    def open_close(self):
        raise NotImplementedError
