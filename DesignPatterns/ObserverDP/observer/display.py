from DesignPatterns.ObserverDP.observer.observer import Observer


class Display(Observer):

    def update(self, temp, humidity):
        print(f"Temp: {temp} and Humidity: {humidity} from display")
