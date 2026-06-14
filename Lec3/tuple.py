# Tuples in Python
# A built-in data type that lets us create immutable sequences of values.

tup = (1, 2, 3, 4, 5)
print(type(tup))
print(tup[0])
# tup[0] = 55 Not Allowed

empty_tup = ()
print(type(empty_tup))
print(empty_tup)

single_tup = (1, )
print(type(single_tup))
print(single_tup)

# Tuple slicing same as list or strings
print(tup[1:3])