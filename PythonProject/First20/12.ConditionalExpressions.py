# conditional expressions = A one-line shortcut for the if-else statment (ternary operators)
#                           print or assign one of two values based on a condtion
#                           X if condition else Y

num = 5
a = 16
b = 7
age = 13
temperature = 20
user_role = "gust"
print("Positive" if num > 0 else "Negative")
result = "even" if num % 2 == 0 else "odd"
max_num = a if a > b else b 
min_num = a if a < b else b
status = "adult" if age > 18 else "child"
weather = "hot" if temperature > 20 else "cold"
access_level = "Full Access" if user_role == "admin" else "Limeted Access"
