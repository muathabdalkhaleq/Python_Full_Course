# iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop


#######################################################
print("---------dictionary---------")
print()
my_dictionary = {"A":1,
                 "B":2,
                 "C":3}

for key,value in my_dictionary.items() :
    print(f"{key:<6}:{value:>6}")

print()
print()
#######################################################
print("---------String---------")
print()

name = "Muath Abdalkhaleq"

for char in reversed(name):
    print(char,end=" ")

print()
print()
#######################################################
print("---------Set---------")
print()

fruits = {"apple","orange","banana","cocunt"}
#for fruit in reversed(fruits) :
# TypeError: 'set' object is not reversible
for fruit in fruits :
    print(fruit)

print()
#######################################################
print("---------list and Tuple---------")
print()
numbers = (1,2,3,4,5)
#numbers = [1,2,3,4,5]

#for number in reversed(numbers):
for number in numbers:
    print(number,end=" - ")
print()
print()