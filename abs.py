from abc import ABC, abstractmethod

#------ Abstraction ------#
'''
Purpose:            Hides internal details and shows only functionalities
                    ex: not need to know how engine works, but can still drive a car

Abstract Class:     Contain one or more abstract methods, cannot be instantiated, require subclasses to provide implementation
                    for the abstract methods.

Abstract Method:    Methods that are declared but contains no implementation, require subclasses for implementation

Python does not come with abstract classes by default but this can be achieved with module: from abc import ABC, abstractmethod
'''

# decorator (@) allows to add new functionality to an existing obj (classes, methods, functions) w/o modifying its structure
class Shape(ABC):
    @abstractmethod #makes method abstract!
    def area(self):
        pass #no implementation (empty method)
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side
    def area(self): #these methods need to be here from parent class or we cannot instantiate!!
        return self.__side*self.__side
    def perimeter(self): #these methods need to be here from parent class or we cannot instantiate!!
        return 4 * self.__side

#myshape = Shape() #cannot do this because it's an abstract class!
mysquare = Square(5) #should receive the same error, because it is inheriting from abstract class!
print(mysquare.area())
print(mysquare.perimeter())
