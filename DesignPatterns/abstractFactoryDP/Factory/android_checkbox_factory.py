from DesignPatterns.abstractFactoryDP.Factory.factoryAbc import Factory
from DesignPatterns.abstractFactoryDP.UIElements.android_chcekbox import AndroidCheckBox


class AndroidCheckBoxFactory(Factory):
    def create(self):
        return AndroidCheckBox()