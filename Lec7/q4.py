'''
From a file containing numbers separated by comma, print the count of even numbers.
'''

with open("q4Practice.txt", "r") as f:
    data = f.read()
    print(data)
    list = []
    num = ""
    for i in data:
        if i == ",":
            print(num)
            list.append(int(num))
            num = ""
        else:
            num += i
    print(int(num))
    list.append(int(num))

    count = 0
    for val in list:
        if val % 2 == 0:
            count += 1
    print("Total" , count , "Even Numbers")
