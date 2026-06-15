# WAP to find the sum of first n numbers. (using while)
n = int(input("Enter the number : "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1

print("The sum upto n is : " , sum)