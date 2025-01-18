class Parent:
    def __init__(self):
        pass

    def func(self):
        print("parent 1..")

class Child1(Parent):
    def __init__(self):
        pass

    def func_child(self):
        print("child 1..")


class Child2(Parent):
    def __init__(self):
        pass


# c2 = Child2()
# c2.func_child()  -> error

c2 = Child1()
c2.func_child()