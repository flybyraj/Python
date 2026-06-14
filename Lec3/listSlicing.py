# List Slicing Similar to String Slicing

# list_name[ start_index : ending_index ] # ending_index not included

marks = [54, 58, 47, 49, 78]

print(marks[ 1:4 ])
print(marks[  : 4])   #marks[0:4]
print(marks[ 1:  ])   #marks[1:4]
print(marks[ -3:-1])