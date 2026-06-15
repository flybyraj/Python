''' 
ABSRACTION
ENCAPSULATION
INHERITANCE
POLYMORPHISM
'''

# Abstraction :  Hiding the implementation details of a class and only showing the essential features to the user.

class Car():
    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False

    def car_start(self):
        self.acc = True
        self.brake = True
        self.clutch = True
        print("Car Started")

car1 = Car()
car1.car_start()

# Encapsulation : Wrapping data and function into a single unit(Object).

