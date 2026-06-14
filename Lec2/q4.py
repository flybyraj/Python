# WAP to find greatest of 3 numbers entered by user

num1 = int(input("Enter Num1 : "))
num2 = int(input("Enter Num2 : "))
num3 = int(input("Enter Num3 : "))

if num1 > num2:
    if num1 > num3:
        print(num1 , "is Greatest.")
    elif num1 < num3:
        print(num3 , "is Greatest")
elif num2 > num3:
    print(num2 , "is Greatest")
else:
    print(num3 , "is Greatest.")