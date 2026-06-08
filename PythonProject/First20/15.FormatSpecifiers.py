# format specifiers = {value:flags} format a value based on what
#                               flags are inserted
# ---------------------------------------------------------------
# ---------------------------------------------------------------
# ---------------------------------------------------------------
# .(number)f = round to that many decimal places (fixed point)
# (number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# < = left justify
# > = right justify
# ^ = center align
# + = use a plus sign to indicate positive value
# = = place sign to leftmost position
#   = insert a space before positive numbers
# , = comma separator

price1 = 32222.14159
price2 = -98227.65
price3 = 1222.34

print(f"price 1 is ${price1:.2f}")
print(f"price 2 is ${price2:.2f}")
print(f"price 3 is ${price3:.2f}")
print("-----------------------------------------")
print(f"price 1 is ${price1:10}") #each value have 10 spaces
print(f"price 2 is ${price2:10}")
print(f"price 3 is ${price3:10}")
print("-----------------------------------------")
print(f"price 1 is ${price1:010}") #each value have 10  with 0
print(f"price 2 is ${price2:010}")
print(f"price 3 is ${price3:010}")
print("-----------------------------------------")
print(f"price 1 is ${price1:<10}") #left
print(f"price 2 is ${price2:^10}") #center
print(f"price 3 is ${price3:>10}") #right
print("-----------------------------------------")
print(f"price 1 is ${price1:+}") 
print(f"price 2 is ${price2:+}") 
print(f"price 3 is ${price3:+}") 
print("-----------------------------------------")
print(f"price 1 is ${price1: }") 
print(f"price 2 is ${price2: }") 
print(f"price 3 is ${price3: }") 
print("-----------------------------------------")
print(f"price 1 is ${price1:,}") 
print(f"price 2 is ${price2:,}") 
print(f"price 3 is ${price3:,}") 


print("-----------------------------------------")
print("-----------------------------------------")
print("-----------------------------------------")
print("-----------------------------------------")
print(f"price 1 is ${price1:+,.2f}")
print(f"price 2 is ${price2:+,.2f}")
print(f"price 3 is ${price3:+,.2f}")

