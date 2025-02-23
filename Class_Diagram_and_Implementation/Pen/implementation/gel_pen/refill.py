from Class_Diagram_and_Implementation.Pen.implementation.pen_abs.ink import Ink


class Refill(Ink):

    def __init__(self, color: str, density: float):
        super().__init__(color, density)

    def refill(self):
        return f"This refill is for gel pen and of {self._color} color with density {self._density}"

    def set_color(self, color: str):
        self._color = color

    def set_density(self, density: str):
        self._density = density

    def get_color(self):
        return self._color

    def get_density(self):
        return self._density


