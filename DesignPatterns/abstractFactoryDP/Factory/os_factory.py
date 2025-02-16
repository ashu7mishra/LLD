from DesignPatterns.abstractFactoryDP.Factory.abstract_IOS_factory import AbstractIOSFactory
from DesignPatterns.abstractFactoryDP.Factory.abstract_android_factory import AbstractAndroidFactory


class OSFactory:

    def create_type(self, val):
        if val.upper() == "IOS":
            abs = AbstractIOSFactory()

        if val.upper() == "ANDROID":
            abs = AbstractAndroidFactory()

        return abs