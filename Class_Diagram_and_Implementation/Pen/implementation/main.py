from Class_Diagram_and_Implementation.Pen.implementation.gel_pen.closingType import ClosingType
from Class_Diagram_and_Implementation.Pen.implementation.gel_pen.gelPen import GelPen


if __name__ == "__main__":
    gel_pen = GelPen('Reynold', 'Reynold', 10, 'blue', 0.1)

    print(gel_pen.write())
    print(gel_pen.open_close())
    print(gel_pen.get_price())
    print(gel_pen.get_brand())
    print(gel_pen.get_name())
    print(gel_pen.get_closing_type())
    print(gel_pen.get_type())
    print(gel_pen.refill())
    print(gel_pen.get_color())
    print(gel_pen.get_density())

    gel_pen.set_price(20)
    gel_pen.set_brand('classmate')
    gel_pen.set_name('mountain top')
    gel_pen.set_closing_type(ClosingType.ROTATE)
    gel_pen.set_type('ball pen')
    gel_pen.set_color('green')
    gel_pen.set_density(0.2)
    gel_pen.refill()

    print(gel_pen.write())
    print(gel_pen.open_close())
    print(gel_pen.get_price())
    print(gel_pen.get_brand())
    print(gel_pen.get_name())
    print(gel_pen.get_closing_type())
    print(gel_pen.get_type())
    print(gel_pen.refill())
    print(gel_pen.get_color())
    print(gel_pen.get_density())
