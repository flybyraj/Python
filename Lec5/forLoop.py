# For Loops in Python are used for Sequential Traversal for traversing list , string , tuples, etc.

list = [1,2,3,4]
for el in list:
    print(el)

veggies = ["potato", "tomato"]
for veg in veggies:
    print(veg)       #work
else:
    print("finished") #work when loop ends


name = "Raj Sharma"
for char in name:
    if char == "k":
        print("S Found")
        break #else ko bhi execute nhi hone dega
    print(char)
else:           #work when loop ends(pura chal ke)
    print("END")

