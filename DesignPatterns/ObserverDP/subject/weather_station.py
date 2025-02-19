from DesignPatterns.ObserverDP.subject.subject import Subject


class WeatherStation(Subject):

    def __init__(self):
        super().__init__()
        self.temp = 0
        self.humidity = 0

    def updateWeather(self, temp, humidity):
        self.temp = temp
        self.humidity = humidity
        self.notify(temp, humidity)