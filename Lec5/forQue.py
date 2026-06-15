# Print the elements of the following list using a for loop:
'''
list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for el in list :
    print(el)
'''


# Search for a number x in this tuple using for loop:
tuple = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
x = int(input("Enter the number : "))
index = 0
for num in tuple:
    if num == x:
        print("Number Found!!! at index : " , index)
        break
    index += 1