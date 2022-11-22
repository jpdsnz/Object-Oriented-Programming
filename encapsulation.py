#------ Encapsulation ------#
# restricting acceess to methods and vars to prevent direct data modification
# public methods/vars are accessible from anywhere in program
# private methods/vars are accessible from their own class


class Cars:
    def __init__(self, speed, color):
        self.__speed = speed #double underscore makes variable private!
        self.__color = color #double underscore makes variable private!

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed
 
ford = Cars(250, "green")
nissan = Cars(300, "red")
toyota = Cars(350, "blue")

ford.set_speed(450) #change value

ford.speed = 500 # this will get ignored because variable is private

ford.set_speed(750) #change value

print(ford.get_speed())
#print(ford.__color) # cannot print because private!
