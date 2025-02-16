from DesignPatterns.abstractFactoryDP.Factory.factoryAbc import Factory
from DesignPatterns.abstractFactoryDP.UIElements.ios_button import IOSButton


class IOSButtonFactory(Factory):

    def create(self):
        return IOSButton()