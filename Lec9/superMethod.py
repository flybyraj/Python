# Super Method
# SUper() method is used to access methods of parent class.

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")

class Toyota(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()


car1 = Toyota("Prius", "Electric")
print(car1.name)
print(car1.type)