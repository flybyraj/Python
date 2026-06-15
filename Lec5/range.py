# Range is a Function that returns a sequence of numbers , starting from 0 by default , and increments by 1 (by default) , and stops before a specified number.

# Range(start? , stop , step?)

seq = range(5) # range(stop)
for i in seq:
    print(i)
print("END")


for i in range(2, 10): #range(start, stop)
    print(i)
print("END")

for i in range(2, 10, 2): #range(start, stop, step)
    print(i)
print("END")

# print even numbers from 2 to 100 using range
for i in range(2, 100, 2):
    print(i)
print("Even numbers printed")