from car import car

# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# calss = (blueprint) used to design the structure and layout of an object

car1 = car("Opel",2014,"gry",True)
car2 = car("Corvette",2025,"blue",True)
car3 = car("Skoda",2026,"red",False)

print(car1.color)
car1.describe()