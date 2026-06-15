f = open("demo.txt", "r")
# data = f.read() # f.read() reads entire file
# print(data)


line1 = f.readline() # f.readline() reads one line at a time
line2 = f.readline()
print("Line1", line1)
print("line2", line2)
f.close()