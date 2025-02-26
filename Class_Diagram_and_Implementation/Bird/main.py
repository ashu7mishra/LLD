from Ostritch.Ostrich import Ostrich
from Sparrow.Sparrow import Sparrow

if __name__ == "__main__":

    ostrich = Ostrich(name='Ostrich', color='white', height='3m', weight='30kg', wings='2')

    print(ostrich.run())
    print(ostrich.eat())
    print(ostrich.get_name())
    ostrich.set_name('Australian Ostrich')
    print(ostrich.get_name())
    print(ostrich.move())

    sparrow = Sparrow(name='Sparrow', color='brown', height='10cm', weight='100kg', wings='2')

    print(sparrow.fly())
    print(sparrow.eat())
    print(sparrow.get_name())
    sparrow.set_name('Indian Sparrow')
    print(sparrow.get_name())
    print(sparrow.move())