
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


car = Car()
plane = Plane()


car.move()   
plane.move()  
