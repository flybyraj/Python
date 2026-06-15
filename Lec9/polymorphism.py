# Polymorphism : Operator Overloading
# When the same operator is allowed to have different meaning according to the context.
# Dunder functiion __fn__()



print(1+2) #sum
print("Raj"+"Sharma") #concatenate
print([1,2,3]+[4,5,6]) #merge 

# complex numbers

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2): # Dunder FUnction
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)


    def __sub__(self, num2): # Dunder Function
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
    

num1 = Complex(5,3)
num1.showNumber()

num2 = Complex(7,5)
num2.showNumber()

num3 = num1 + num2
print(num3.showNumber())

num4 = num1 - num2
print(num4.showNumber())