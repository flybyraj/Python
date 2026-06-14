set = {1,2,3,4,4,5}

# Add an element
set.add(9)
set.add("Raj")
set.add((1,2,3)) # tuple can be added in set
# set.add([1,2,3]) # list cant be added in set
# Immutable -> Hashable can be aded in set eg. tuple,int
# Hashable -> Dict, List , Sets
print(set)

# remove an element
set.remove(5)
print(set)

#Empties an set
# set.clear()
# print(set)
# print(len(set))

# Removes a random value
print(set.pop())

#combine both set value and return new
set1 = {1,2,3,4,4,4,5}
set2 = {5,6,7,8,8}
print(set1.union(set2))

#combine common values and return new
print(set1.intersection(set2))