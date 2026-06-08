# while loop = excute some code WHILE some condition remains true 

num = int(input("Enter a number between 1- 10 : "))
while num < 1 or num > 10:
    print (f"{num} is not valid")
    num = int(input("Enter a number between 1- 10 : "))
print(f"Your number is {num}")


""" EX 3
food = input("Enter a food you like (q to quit)")

while not food == "q" :
    print(f"you like {food}")
    food = input("Enter a food you like (q to quit)")
print("bye")
""" 

""" EX 2 :
age = int(input("Enter your age"))
while age < 0 :
    print("age can't be negative ")
    age = int(input("Enter your age"))
    
print(f"you are {age} years old")
"""

""" EX 1 :
name = input("Enter your name : ")

while name == "":
    print("you did not enter your name ")
    name = input("Enter your name : ")
print(f"Hellow {name}") 

"""