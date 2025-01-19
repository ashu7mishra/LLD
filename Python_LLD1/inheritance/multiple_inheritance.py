class Parent1:
    def __init__(self):
        self.nose = 1

    def func(self):
        print('Parent 1')


class Parent2:
    def __init__(self):
        self.name = 'abc'

    def func(self):
        print('Parent 2')

class Child(Parent1, Parent2):
    def __init__(self):
        # super().__init__() or

        Parent1.__init__(self)
        Parent2.__init__(self)


# class Child2(Parent1, Parent2):
#     def func(self):
#         super().func()

c = Child()
c.func()
# Parent2.func(c)

print(c.name) #error
print(c.nose)

# c1 = Child2()
# c1.func()

# print(dir(c))
# print(Child.mro())
# print(Child.__mro__)