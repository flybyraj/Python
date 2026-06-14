student = {
    "name" : "Raj Sharma",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "bio" : 95,
    }
}

# Return all Keys
print(student.keys()) 
print(student["subjects"].keys())

#typecast in list
print(list(student.keys()))

#total no of key:value pairs
print(len(student)) #or
print(len(list(student.keys())))

# Return all values
print(student.values())
print(list(student.values()))

# Return all key:value pairs
print(student.items())
pairs = list(student.items())
print(pairs[0])

# Return the value a/q to the key
print(student.get("name"))
print(student["name"])
# reason , name2 dont exist
# print(student.get("name2")) #None
# print(student["name2"])     #Error

# insert specific items into dictionary
new_dict = {
    "name" : "Prince" , # updates name value 
    "age" : 20,
}
student.update(new_dict)
student.update({"city" : "delhi"}) # add new key:value pair
print(student)