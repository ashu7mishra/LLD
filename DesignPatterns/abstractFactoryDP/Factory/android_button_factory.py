from DesignPatterns.abstractFactoryDP.Factory.factoryAbc import Factory
from DesignPatterns.abstractFactoryDP.UIElements.android_button import AndroidButton


class AndroidButtonFactory(Factory):
    def create(self):
        return AndroidButton()

