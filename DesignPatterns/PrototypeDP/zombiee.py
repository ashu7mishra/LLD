from DesignPatterns.PrototypeDP.monstor import Monstor
import copy


class Zombiee(Monstor):

    def __init__(self, health):
        self.health = health

    def attack(self):
        print("Attacking.....")

    def clone(self):
        return copy.deepcopy(self)

