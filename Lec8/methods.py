# Methods are function that belongs to objects.

# class consiste of :  1.Data(Attribute) 2.Methods(Functions)

# Creating class

class Student:
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks

    def hello(self):
        print("hello", self.name)

    def get_marks(self):
        print("Marks : ", self.marks)

# Creating Object

s1 = Student("karan", 89)
s1.hello()
s1.get_marks()