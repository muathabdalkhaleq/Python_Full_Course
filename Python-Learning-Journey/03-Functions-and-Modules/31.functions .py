# function = A block of reusable code 
#            place () after the function to invoke it 

def happy_birthday(name,age):
    print (f"Happy birthday to {name} ")
    print(f"you are {age}!")
    print()

# happy_birthday("Bro",15)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due : {due_date}")

# display_invoice("muath" ,100.01, "01/02")

def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

print(create_name("muath","ahmed"))