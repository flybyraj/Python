#Write a recursive funvtion to calculate sum of first n natural numbers.

def sum(a):
    if a == 0:
        return 0
    return a + sum(a-1)

print(sum(5))