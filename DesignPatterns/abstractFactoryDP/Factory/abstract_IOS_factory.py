from DesignPatterns.abstractFactoryDP.Factory.ios_button_factory import IOSButtonFactory
from DesignPatterns.abstractFactoryDP.Factory.ios_check_box_factory import IOSCheckBoxFactory


class AbstractIOSFactory:

    def create_button(self):
        return IOSButtonFactory()

    def create_checkbox(self):
        return IOSCheckBoxFactory()