from vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, number_of_tyres, color):
        super().__init__(number_of_tyres)
        self.color = color

    def start(self):
        print("Car started by ignition.")


car = Car(4, 'red')
car.start()
print(f"The {car.color} color car has {car.number_of_tyres} tyres.")