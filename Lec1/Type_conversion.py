#Type conversion - automatically
a = 2
b = 4.5

sum = a + b # int to float because float is superior
print("Type conversion: ", sum)

# Type casting - manually
a = float("2")
b = 4.5
print("Type casting :" , a + b)

z = 3.14
z = str(z)
print(type(z))