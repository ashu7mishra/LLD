from non_flyable.NonFlyable import NonFlyable


class Ostrich(NonFlyable):

    def eat(self):
        return "Ostrich eats weeds"

    def make_sound(self):
        return "Ostrich sounds like trr trr"

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_height(self, height):
        self._height = height

    def get_height(self):
        return self._height

    def set_weight(self, weight):
        self._weight = weight

    def get_weight(self):
        return self._weight

    def set_wings(self, wings):
        self._wings = wings

    def get_wings(self):
        return self._wings

    def run(self):
        return "Ostrich don't fly. They run"

    def move(self):
        return "Ostrich move fast"




