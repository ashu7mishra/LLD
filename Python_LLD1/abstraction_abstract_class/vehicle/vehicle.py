from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, number_of_tyres):
        self.number_of_tyres = number_of_tyres

    @abstractmethod
    def start(self):
        pass

# v = Vehicle(3)
# v.start()