from abc import ABC, abstractmethod

from bird.Bird import Bird


class NonFlyable(Bird):

    @abstractmethod
    def run(self):
        raise NotImplementedError

    @abstractmethod
    def move(self):
        raise NotImplementedError
