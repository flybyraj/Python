# RECURSION is when a function calls itself repeatedly.

def show(n):
    if n==0:  # Base case
        return
    print(n)
    show(n-1)
    print("END" ,n )

show(5) # 5,4,3,2,1

