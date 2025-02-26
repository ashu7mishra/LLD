from non_flyable.NonFlyable import NonFlyable


class DontFly(NonFlyable):

    def run(self):
        return "Ostrich don't fly. They run"

    def move(self):
        return "Ostrich move fast"
