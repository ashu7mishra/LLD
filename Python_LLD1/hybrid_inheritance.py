class Parent:
    def __init__(self):
        self.eyes = 2

    def display(self):
        print("Parent Class")

    def display(self, a):
        print("a displayed")


class Child(Parent):

    def __init__(self, age):
        # self.eyes = 1
        super().__init__()
        self.eyes = 1
        self.age = age

    def display(self):
        super().display(3)
        print("Child display")

class GrandChild1(Child):
    pass

class GrandChild2(Child):
    pass


gc1 = GrandChild1(10)
gc2 = GrandChild2(12)

print(gc1.eyes)
