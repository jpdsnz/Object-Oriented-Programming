class Instructors:
    companyName = "Bluelime"

    def __init__(self,course, duration): #constructor
        self.course = course
        self.duration = duration

    def printinfo(self):
        print("My Company name is ", self.companyName)

    def printcourse(self):
        print(self.course)

elearning = Instructors("Python for Beginners", 7)

bls = Instructors("Django for beginners", 8)

bls.course = "HTML"

bls.printinfo() #calling a method(class function)
#bls.printcourse()
#del bls.duration #Delete an item from object, careful!
print(bls.course) #Accessing data
print(bls.duration) #Accessing data

#------- Class vs instance ------ #

#This is a multi-line comment with docstrings
"""
Class:      defined outside any method, accessed outside class with className, Not prefixed,
    Modifications affects all class instances, Classes are indented

Instance:   Defined inside class methods, accessed outside class with objectName, prefixed
    with self keyword, modifications to object is local, instances are not indented
"""
