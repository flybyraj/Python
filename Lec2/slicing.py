### SLICING Accessing parts of a string

# str[starting_idx : ending_idx] # Ending index not included

str = "Raj Sharma"
print(str[0 : 3]) # Raj
print(str[0 : len(str)])
print(str[0 : ]) # str[0 : len(str)]
print(str[ : 5]) # str[0 : 5]

# Negative Index
'''
 A p p l e
-5-4-3-2-1

'''
str = "Apple"
print(str[-3 : -1]) # -1 not included
print(str[-4 : ])
print(str[ : -2])