# Property
# We use @property Decorator on any method in class to use the method as a property.

class Student:
    def __init__(self, phy, chem, maths):
        self.chem = chem
        self.maths = maths
        self.phy = phy 
    #     self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths)/3) + "%"

stu1 = Student(88, 78,98)
print(stu1.percentage)

stu1.phy = 80
print(stu1.phy)
# stu1.calcPercentage()
print(stu1.percentage)