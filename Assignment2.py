#Task 2
traffic_light = "Green"

class Vehicle:
    vehicle_count = 0

    def __init__(self, name):
        self.name = name
        Vehicle.vehicle_count += 1

    def start_engine(self):
        message = "Engine started"
        print(message)


class Car(Vehicle):
    def __init__(self, name, make):
        super().__init__(name)
        self.make = make

    def start_engine(self):
        message = "Car engine started"
        print(message)
        print(f"Traffic light is {traffic_light}")


class Bike(Vehicle):
    def __init__(self, name, typeBike):
        super().__init__(name)
        self.typeBike = typeBike

    def start_engine(self):
        message = "Bike engine started"
        print(message)
        print(f"Traffic light is {traffic_light}")


car = Car("Mustang", "Ford")
car.start_engine()

bike = Bike("R15", "Sport")
bike.start_engine()

print(f"Total number of vehicles: {Vehicle.vehicle_count}")
