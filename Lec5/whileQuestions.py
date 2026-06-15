# Print numbers from 1 to 100.
'''
i = 1
while i <= 100 :
    print(i)
    i +=1
'''

# Print numbers from 100 to 1.
'''
i = 100
while i >= 1:
    print(i)
    i -= 1
'''

# Print the multiplication table of a number n.
'''
i = 1
n = int(input("Enter the Number : "))
while i <= 10:
    print(n*i)
    i += 1
'''

# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
'''
i = 1
list = []
while i <= 10:
    list.append(i**2)
    i += 1
print(list)
'''
'''
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1
'''

# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

tuple = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i = 0
x = int(input("Enter the Number : "))
while i < len(tuple):
    if x == tuple[i]:
        print("The number" , x , "found at Index" , i)
        break
    else:
        print("FInding")
    i += 1