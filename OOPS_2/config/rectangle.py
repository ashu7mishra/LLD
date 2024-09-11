import copy

from config.point import Point


class Rectangle:
    def __init__(self, *args):
        """
        Initialize a Rectangle object.

        Args:
            *args: Variable number of arguments. The constructor can be called in three ways:
                - With two Point objects representing the top-left and bottom-right corners.
                - With four integers representing the x and y coordinates of the top-left and bottom-right corners.
                - With a single Rectangle object for copying.

        Raises:
            ValueError: If invalid arguments are provided.
        """
        if len(args) == 2:
            self.topLeft = copy.deepcopy(args[0])
            self.bottomRight = copy.deepcopy(args[1])

        elif len(args) == 4:
            self.topLeft = Point(args[0], args[1])
            self.bottomRight = Point(args[2], args[3])

        elif len(args) == 1 and isinstance(args[0], Rectangle):
            self.topLeft = copy.deepcopy(args[0].topLeft)
            self.bottomRight = copy.deepcopy(args[0].bottomRight)

        else:
            raise ValueError()

