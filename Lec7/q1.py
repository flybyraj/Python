'''
Create a new file "practice.txt" using python. Add the following data in it:

Hi everyone
we are learning File I/O

using Java.
I like programming in Java.
'''

f = open("practice.txt", "w")
f.write("Hi Everyone \n")
f.write("we are learning File I/O \n \n")
f.write("using Java.\n")
f.write("I like programming in Java.")

f.close()