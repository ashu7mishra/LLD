from abc import abstractmethod

from bird.Bird import Bird


class Flyable(Bird):

    @abstractmethod
    def fly(self):
        raise NotImplementedError

    @abstractmethod
    def move(self):
        raise NotImplementedError
