# using for & range( )
# Print numbers from 1 to 100.
for i in range(1, 101):
    print(i)
print("Printed 1 to 100")


# Print numbers from 100 to 1.
for i in range(100, 0, -1):
    print(i)
print("Printed 100 to 1")


# Print the multiplication table of a number n.
n = int(input("Enter the number: "))
for i in range(1, 11):
    print(n*i)
print("Table of n printed")