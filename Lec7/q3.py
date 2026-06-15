# Search if word "learning" exist in the file or not.
# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if (data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")


'''
WAF to find in which line of the file does the word "learning"occur first.
Print -1 if word not found.
'''
def check_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                return line_no
            line_no += 1
    return -1

print(check_line())