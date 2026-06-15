# OOP in Python
# To map with real world scenario , we started using objects in code.
# This is called Object Oriented Programming.
# Procedural(repetition) --> Functional(reusability) --> OOP(Object & Classes)

# Class is a blueprint for creating Objects.

#creating classes
class Student:
    name = "Raj Sharma"

#creating object (instance)
s1 = Student()
print(s1.name)

s2 = Student()
print(Student.name)

class Car:
    color = "blue"
    brand = "BMW"

car1 = Car()
print(car1.color)
print(car1.brand)