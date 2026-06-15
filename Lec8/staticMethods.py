# Methods that dont use the self parameter (work at class level).

class Student():


    def __init__(self , name , maths, chem, phy):
        self.name = name
        self.maths = maths
        self.chem = chem
        self.phy = phy

    @staticmethod # Class Method # Decorator
    def hello():
        print("Hello")

    def avg_marks(self):
        return (self.maths + self.phy + self.chem)/3

s1 = Student("RAJ" , 89, 78 , 98)
print(s1.name, s1.avg_marks())
s1.hello()


# Decorator allows us to wrap another function in order to extend the behaviour of the wrapped function , without permanently modifying it.