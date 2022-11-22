#------ Polymorphism ------#
"""
def addNumbers(a,b,c=1):
    return a + b + c

print(addNumbers(8,9)) # should get 18 here!

print(addNumbers(8,9,4))
"""

class UK():
    def capital_city(self):
        print("London is the capital of UK")

    def language(self):
        print("English is the primary language ")

class Spain():
    def capital_city(self):
        print("Madrid is the capital of UK")

    def language(self):
        print("Spanish is the primary language ")

def europe(eu):
    eu.capital_city()


queen = UK()
#queen.capital_city()

zara = Spain()

europe(queen)
europe(zara)
#zara.capital_city()

'''
for country in (queen,zara):
    country.capital_city()
    country.language()
'''
