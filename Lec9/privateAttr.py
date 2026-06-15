# Private(like) attributes & methods
# Conceptual implementation in Python.
# Private attributes and methods are meant to be used only eithin the classes and not accessible from outside the class.
# self.__attr private attr
# def __method(): private method


class Account:
    def __init__(self, acc_no, acc_pwd):
        self.acc_no = acc_no
        self.__acc_pwd = acc_pwd

    def reset_pwd(self):
        print(self.__acc_pwd)


acc1 = Account("12345", "abcde")

print(acc1.acc_no)
# print(acc1.__acc_pwd)

acc1.reset_pwd()


class Person():
    __name = "raj" # Private Attr

    def __hello(self): # Private Method
        print("Hello")

    def welcome(self):
        self.__hello()
        print(self.__name)

p1 = Person()
# print(p1.__name)
# p1.hello()
p1.welcome()