#Dictonary are used to store data values in Key:value pairs
#They are unordered , mutable(changable) & dont allow duplicate keys.
#Key cannot be changed.

dict = {
    "name":"Raj",
    "cgpa":8.0,
    "age": 22,
    "is_adult": True,
    "subjects": ["Python", "C", "Java"],
    "topics": ("dict", "set")
}

print(dict["name"])
dict["name"] = "Raj Sharma" # Change value Overwrite
dict["number"] = 9693 # add new key:value pair
print(dict["name"])
print(dict["cgpa"])
print(dict["age"])
print(dict)

null_dict = {}
null_dict["name"] = "Raj Sharma"
print(null_dict)