# Arithmetic Operators
a = 6
b = 2

print(a + b)   #sum
print(a - b)   #diff
print(a * b)   #multiplication
print(a / b)   #division  float
print(a ** b)  #Exponent
print(a % b)   #Modulo Remainder

# Relational Operator
a = 50
b = 20

print(a == b) #False
print(a != b) #True
print(a >= b) #True
print(a > b) #True
print(a <= b) #False
print(a < b) #False

# Assignment Operator
num = 10
num += 10  # num = num + 10
print("num : ",num)
   # same for (+= , -= , *= , /= , %= , **=)


# Logical Operators (not,and,or)
a,b=50,30
print(not False)
print("a :",a)
print("b :",b)
print(not (a > b))

val1 = True
val2 = False
print("AND operator :", val1 and val2)
print("OR operator :", val1 or val2)
print("OR operator :", (a == b) or (a > b))