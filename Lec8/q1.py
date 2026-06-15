'''
Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average.
'''

class Student():

    #Paramterized Constructor
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def avg_marks(self):
        sum =0
        for val in self.marks:
            sum += val
        return sum/3

s1 = Student("RAJ" , [89, 78 , 98])
print(s1.name, s1.avg_marks())

s1.name = "Prince" # updating object attribute
print(s1.name)