#------ Inheritance ------#
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Lawyers(Person): #if you create a child class w/o init method, it inherits all methods and attributes of the parent class
    def __init__(self, fname, lname, casetype):
        Person.__init__(self, fname, lname) #reference the parent properties
        self.casetype = casetype;
        #self.firstname = fname
        #self.lastname = lname

    def printinfo(self):
        print("Hello, my name is ", self.firstname, self.lastname)


florist = Person("Jane", "Flowers") #new instantiation
florist.printname()

happy_lawyers = Lawyers("Jack", "Smiley", "criminal")
#happy_lawyers.printinfo() #able to access function from parent!
happy_lawyers.printinfo()
print(happy_lawyers.casetype)
