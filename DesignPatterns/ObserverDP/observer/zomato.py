from DesignPatterns.ObserverDP.observer.observer import Observer


class Zomato(Observer):

    def update(self, temp, humidity):
        if temp > 20:
            print("Zomato updated price of delivery...")