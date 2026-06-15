f = open("demo.txt", "r+") # r+ to overwrite from starting .Stream is positioned at beginning of file.
f.write("ABC")
print(f.read())
f.close()

f = open("demo.txt" , "w+") # w+ to truncate(clear) file and then write . Stream is positioned at beginning of file.
f.write("Truncating with w+")
f.close()

f = open("demo.txt", "a+") # a+ open for reading and writing . Stream is positioned at end of file.f.write()
f.write("abc")
f.close()

'''
r+ read + overwrite pointer(start) - No Truncate
w+ read + overwrite pointer(start) - Truncate
a+ read + append    pointer(end)   - No Truncate
'''