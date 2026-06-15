# Multiple Inheritance
# Base Class inherits Attr or methods from morethan one parent classes.

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A , B):
    varC = "Welcome to calss C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)