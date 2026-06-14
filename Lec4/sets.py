### Set in Python is a collection of the unordered items.
### Each item in the set must be unique and immutable.

# Set is Mutable
# Elements of sets are immutable.

nums = {1,2,3,4}
set2 = {1,2,2,2,3,4}

# int , float,str,tuple.bool can be stored in set.
# list , dict cant be stored in set since mutable.

collection = {1,2,3,4,4,4,"hello","Raj"}


print(collection)
print(type(collection))
print(len(collection)) # total no of items

empty_dict = {} # Empty Dictionary
empty_set = set() # Empty Set