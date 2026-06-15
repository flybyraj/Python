# WAP to find the factorial of first n numbers. (using for)

n = int(input("Enter the number : "))
fact = 1
for i in range(1, n+1):
    fact *= i

print("Factorial upto n is : ", fact)