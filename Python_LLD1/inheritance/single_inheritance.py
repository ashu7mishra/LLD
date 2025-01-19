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


c = Child(10)
c.display()
print(c.age, c.eyes)
