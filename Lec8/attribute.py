# Class Attribtute & Instance(Object) Attribute
# Class.attr or obj.attr for Class Attributr
# self.attr for Object attributr


class Student:
    college_name = "ABC"
    name = "anonymous" # Class Attr


    #parameterized constructor
    def __init__(self , name , marks):
        self.name = name  #Obj Attr higher precedence
        self.marks = marks
        print("Adding new Student")

s1 = Student("Raj", "8") # attributes or variables
print(s1.name, s1.marks, s1.college_name)

s2 = Student("Sharma", "9")
print(s2.name, s2.marks , Student.college_name)