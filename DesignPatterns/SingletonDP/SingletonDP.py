import threading

class Singleton:

    __isInstance = None
    __Lock = threading.Lock

    def __new__(cls, *args, **kwargs):
        if cls.__isInstance is None:
            with cls.__Lock:
                if cls.__isInstance is None:
                    cls.__isInstance = super(Singleton, cls).__new__(cls)

        return cls.__isInstance


if __name__ == '__main__':
    s1 = Singleton()
    print(s1)
    s2 = Singleton()
    print(s2)
    print(s1 is s2)