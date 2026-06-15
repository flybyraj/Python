# Multi-Level Inheritance


class Car:
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped")

class Toyota(Car):
    def __init__(self, name):
        self.name = name

class Fortuner(Toyota):
    def __init__(self, type):
        self.type = type


car1 = Fortuner("Diesel")
car1.start()