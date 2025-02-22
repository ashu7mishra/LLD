import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


from Class_Diagram_and_Implementation.Pen.implementation.gel_pen.gelPen import GelPen


if __name__ == "__main__":
    gel_pen = GelPen('Reynold', 'Reynold', 10)

    print(gel_pen.write())
    print(gel_pen.open_close())
    print(gel_pen.get_price())
    print(gel_pen.get_brand())
    print(gel_pen.get_name())
    print(gel_pen.get_closing_type())
    print(gel_pen.get_type())
