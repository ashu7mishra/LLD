from Class_Diagram_and_Implementation.Pen.implementation.pen_abs.pen import Pen
from Class_Diagram_and_Implementation.Pen.implementation.gel_pen.closingType import ClosingType
from Class_Diagram_and_Implementation.Pen.implementation.gel_pen.refill import Refill


class GelPen(Pen, Refill):

    def __init__(self, name: str, brand: str, price: int, color: str, density: float):
        Pen.__init__(self, "Gel Pen", name, brand, price)
        Refill.__init__(self, color, density)
        self._closingType = ClosingType.CAP

    def write(self):
        # raise NotImplementedError
        return "This is a gel pen"

    def open_close(self):
        # raise NotImplementedError
        return f"This pen open - close via {self._closingType}"

    def set_name(self, name):
        # raise NotImplementedError
        self._name = name

    def set_type(self, pen_type):
        self._pen_type = pen_type

    def set_brand(self, brand):
        # raise NotImplementedError
        self._brand = brand

    def set_price(self, price):
        # raise NotImplementedError
        self._price = price

    def set_closing_type(self, closingType):
        # raise NotImplementedError
        self._closingType = closingType

    def get_name(self):
        # raise NotImplementedError
        return self._name

    def get_type(self):
        # raise NotImplementedError
        return self._pen_type

    def get_brand(self):
        # raise NotImplementedError
        return self._brand

    def get_price(self):
        # raise NotImplementedError
        return self._price

    def get_closing_type(self):
        # raise NotImplementedError
        return self._closingType.value