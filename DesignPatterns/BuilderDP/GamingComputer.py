from DesignPatterns.BuilderDP.ComputerBuilder import ComputerBuilder
from DesignPatterns.BuilderDP.computer import Computer


class GamingComputerBuilder(ComputerBuilder):

    def set_cpu(self, cpu):
        if cpu < 2:
            raise ValueError("CPU must be atleast 2")
        self.cpu = cpu

    def set_ram(self, ram):
        self.ram = ram

    def set_gpu(self, gpu):
        self.gpu = gpu

    def set_power_supply(self, power_supply):
        self.power_supply = power_supply

    def set_storage(self, storage):
        self.storage = storage


    def build(self):
        c = Computer()
        c.set_cpu(self.cpu)
        c.set_gpu(self.gpu)
        c.set_ram(self.ram)
        c.set_storage(self.storage)
        c.set_power_supply(self.power_supply)
        return c

