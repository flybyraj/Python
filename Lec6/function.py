# Function in Python Block of staments that perform a specific task.
# To reduce redundancy/repetition

'''defining funcction
def func_name(parameter1, paramtere2,...):
    #some work
    return val

'''

def sum(a, b): # defining function ;  a b are parameters
    sum = a+b
    print(sum)
    return sum

sum(2, 3) # function calling ; 2 and 3 are arguments

def calc_sum(a, b):
    return(a+b)

sum = calc_sum(4,5)
print(sum)

def calc_avg(a, b, c):
    avg = (a+b+c)/3
    print(avg)
    return avg

calc_avg(5, 4, 9)

# built-in function like print() len() type() range()
print("Raj", end=" ")
print("Sharma" ,"CSE", sep= "&")