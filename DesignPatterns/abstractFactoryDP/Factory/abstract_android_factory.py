from DesignPatterns.abstractFactoryDP.Factory.android_button_factory import AndroidButtonFactory
from DesignPatterns.abstractFactoryDP.Factory.android_checkbox_factory import AndroidCheckBoxFactory


class AbstractAndroidFactory:

    def create_button(self):
        return AndroidButtonFactory()

    def create_checkbox(self):
        return AndroidCheckBoxFactory()