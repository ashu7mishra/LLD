from bird_abs.BirdAbs import Bird


class Ostritch(Bird):

    def eat(self):
        return "Ostritch eats weeds"

    def make_sound(self):
        return "Ostritch sounds like trr trr"

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
        raise NotImplementedError

    def get_weight(self):
        raise NotImplementedError

    def set_wings(self, name):
        raise NotImplementedError

    def get_wings(self):
        raise NotImplementedError


