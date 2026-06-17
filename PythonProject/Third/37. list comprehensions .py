# List comprehension = A concise way to create lists in Python
#                    Compact and easier to read than traditional loops
#                    [expression for value in iterable if condition]

grades = [85,42,79,90,56,61,30]
passing_grades = [grade for grade in grades if grade <= 60]

print(passing_grades)


#-----------------------------------------------------------------
# list of numbers with conditions
numbers = [1, -2, 3, -4, 5, -6, 8, -7]

positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]

even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

# print(odd_nums)



#-----------------------------------------------------------------

# char list comprehensions
fruits = ["apple","orange","banana","cocount"]
fruits = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]
# print(fruits)
# print(fruit_chars)

#-----------------------------------------------------------------

# list comprehensions
doubles = [x * 2 for x in range(1,11)]
triples = [y * 3 for y in range(1,11)]
squares = [z * z for z in range(1,11)]
# print(doubles)
# print(triples)
# print(squares)

#-----------------------------------------------------------------

# without list comprehensions
"""
doubles = []
for x in range(1,11):
    doubles.append(x*2)

print(doubles)
"""