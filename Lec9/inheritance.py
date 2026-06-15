# Inheritance : When one class(child/derived) derives the properties & methods of another class(parent/base).

# Single Inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped")

class Toyota(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyota("Fortuner")
car2 = Toyota("Innova")

print(car1.name)
print(car1.start())
print(car1.color)