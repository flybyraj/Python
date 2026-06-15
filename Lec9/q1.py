'''
Qs. Define a Circle class to create a circle with radius r using the constructor.
Define an AreaO method of the class which calculates the area of the circle.
Define a PerimeterO method of the class which allows you to calculate the perimeter of the
circle.
'''
 
class Circle:
    def __init__(self, r):
        self.radius = r

    def Area(self):
        return ((22/7)*self.radius**2)
    
    def Perimeter(self):
        return (2*(22/7)*self.radius)
    
circle1 = Circle(7)
print(circle1.Area())
print(circle1.Perimeter())