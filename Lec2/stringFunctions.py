### Strings function

str = "i am Raj Sharma"

#str.endswith
print(str.endswith("rma")) #return Ture

#str.capitalize
print(str.capitalize()) # Capitalize first letter
print(str)
str = str.capitalize() # Change Orignal String
print(str)

#str.replace(old , new) replace all occurence of old with new
name = "Raj Sharma"
print(str.replace("a" , "Z"))

#str.find(word) return 1st index of occurence
print(name.find("a")) 
print(name.find("Sharma"))
print(name.find("new"))  # not exist -1


#str.count("word")
str = "I am studying Python from Youtube"
print(str.count("Y")) 