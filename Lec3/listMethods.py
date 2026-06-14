#list specific functions are called Methods

list = [2, 1, 3]

# add one element at the end
list.append(4)
print(list)

# Sort in ascending order
list.sort()
print(list)

# Sort in descending order
list.sort( reverse = True)
print(list)
fruit = ["litchi", "Apple", "Banana", "Aaple"]
fruit.sort()
print(fruit)

# reverse List
list.reverse()
print(list)

# insert element at index
#list.insert ( idx , el)
list.insert( 1, 1)
print(list)

# remove first occurence of element
list.remove(1)
print(list)

# remove element at inx
list.pop(3)
print(list)