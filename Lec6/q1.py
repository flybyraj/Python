# WAP to print the lenght of a list .(list is the parameter)

list = [1,2,3,4,5]
list2 = [5,6,7,8]

def print_len(list):
    print(len(list))

print_len(list)
print_len(list2)

#WAF to print the elements of a list in a single line. ( list is the parameter)

def print_el(list):
    for el in list:
        print(el, end=" ")
    print("\n", end="")

print_el(list)
print_el(list2)

#WAP to find the factorial of n.(n is the parameter)


def print_fact(a):
    fact = 1
    for el in range(1, a+1):
        fact *= el
    print(fact)

print_fact(4)


# WAP to convert INR to USD

def inr_to_usd(inr):
    inr /= 100
    print("The USD value is : ", inr)

inr_to_usd(int(input("Enter the INR value: ")))

# ODD or EVEN

def oddeven(num):
    if num %2 ==0:
        print("EVEN")
    else:
        print("ODD")

oddeven(4)
oddeven(3)