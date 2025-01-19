from vehicle import Vehicle

class Bike(Vehicle):

    def __init__(self, number_of_tyres, color):
        super().__init__(number_of_tyres)
        self.color = color

    def start(self):
        print("Bike started by kick.")


bike = Bike(2, 'black')
bike.start()
print(f"The {bike.color} color bike has {bike.number_of_tyres} tyres.")