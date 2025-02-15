from DesignPatterns.BuilderDP.Director import ComputerDirector
from DesignPatterns.BuilderDP.GamingComputer import GamingComputerBuilder

if __name__ == '__main__':
    gb = GamingComputerBuilder()
    director = ComputerDirector(gb)
    director.construct()
    director.get_computer()