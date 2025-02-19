from DesignPatterns.ObserverDP.observer.observerABC import ObserverABC
from abc import abstractmethod


class Observer(ObserverABC):

    @abstractmethod
    def update(self, temp, humidity):
        pass

    def register(self, subject):
        subject.register(self)

    def unregister(self, subject):
        subject.unregister(self)