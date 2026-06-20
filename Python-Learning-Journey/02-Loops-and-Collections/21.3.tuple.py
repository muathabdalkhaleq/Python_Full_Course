# collection = single "variable" used to store multiple values
# List = [] orderd and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ("apple", "orange", "banana", "coconut", "coconut")

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)


# print(fruits.index("coconut"))
print(fruits.count("coconut"))

print(fruits)
# for fruit in fruits:
    # print(fruit)
