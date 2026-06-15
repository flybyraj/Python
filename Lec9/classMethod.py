# Class Method
# A class method is bound to the class & recive the class as an implict first argument.
# Static Method cant access or modify class state & generally used for utility


class Person():
    name = "Any"


    #def changeName(self, name):
        # self.name = name
        # Person.name = name  #class and object attribute changed Method1
        # self.__class__.name = name # Method2

    @classmethod            # decorator ; to change attr of class
    def changeName(cls , name):
        cls.name = name

p1 = Person()
print(p1.name)
p1.changeName("Raj")
print(p1.name)
print(Person.name)

''' 
                    Argument  Use
1. Static Methods    ()       dont change/access any attr. of class or instance(obj)
2. Class Methods     (class)  change/access Class attr
3. Instance Methods  (self)   change/access Instance(obj) attr

'''