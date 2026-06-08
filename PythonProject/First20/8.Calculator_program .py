num1 = float(input ("Enter the first NUMBER "))
operator = input ("Enter the OPERATOR ( +  -  *  / ):")
num2 = float(input("Enter the second NUMBER "))
if operator == "+" :
    print(f"{num1} + {num2} is = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} is = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} is = {num1 * num2}")
elif operator == "/":
    print(f"{num1} / {num2} is = {num1 / num2}")
else :
    print(f"YOU GOT A MISTAKE! {operator} is not valid")
