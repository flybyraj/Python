# Write a recursive function to print all elements in a list.
# Hint: use list and index as parameter

list = [1,2,3,4,5]

def print_el(list,idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_el(list, idx+1)

print_el(list)