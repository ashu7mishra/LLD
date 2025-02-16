from DesignPatterns.abstractFactoryDP.Factory.factoryAbc import Factory
from DesignPatterns.abstractFactoryDP.UIElements.ios_checkbox import IOSCheckBox


class IOSCheckBoxFactory(Factory):

    def create(self):
        return IOSCheckBox()