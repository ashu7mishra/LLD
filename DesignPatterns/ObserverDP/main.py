from DesignPatterns.ObserverDP.observer.display import Display
from DesignPatterns.ObserverDP.observer.zomato import Zomato
from DesignPatterns.ObserverDP.subject.weather_station import WeatherStation

if __name__ == "__main__":

    ws = WeatherStation()

    d1 = Display()

    z = Zomato()

    d1.register(ws)
    z.register(ws)

    ws.updateWeather(10, 50)
    ws.updateWeather(30, 50)
    ws.updateWeather(20, 50)