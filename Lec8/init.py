#init function or Constructor
# All classes have a function called __init__(), which is always executed when the object is being initiated.


class Student:
    

    # default constructor
    def __init__():
        pass

    #parameterized constructor
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks
        print("Adding new Student")

s1 = Student("Raj", "8") # attributes or variables
print(s1.name)
print(s1.marks)

s2 = Student("Sharma", "9")
print(s2.name)
print(s2.marks)