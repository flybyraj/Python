# WAP to check if a list contains a palindrome of elements.
# Use copy() method

list = [1, 2, 9]

copy_list = list.copy()
print(copy_list)
copy_list.reverse()
print(copy_list)

if list == copy_list:
    print("Yes Palindrome")
else:
    print("Not Palindrome")