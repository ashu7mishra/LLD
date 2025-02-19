from DesignPatterns.ObserverDP.observer.observer import Observer
from DesignPatterns.ObserverDP.subject.subjectABC import SubjectABC


class Subject(SubjectABC):

    def __init__(self):
        self.observers = []

    def register(self, observer: Observer):
        self.observers.append(observer)

    def unregister(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, temp, humidity):
        for observer in self.observers:
            observer.update(temp, humidity)