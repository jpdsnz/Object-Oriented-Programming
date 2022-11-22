#------ Inheritance ------#
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Lawyers(Person): #if you create a child class w/o init method, it inherits all methods and attributes of the parent class
    pass #empty method, to inherkit


florist = Person("Jane", "Flowers") #new instantiation
florist.printname()

happy_lawyers = Lawyers("Jack", "Smiley")
happy_lawyers.printname() #able to access function from parent!
