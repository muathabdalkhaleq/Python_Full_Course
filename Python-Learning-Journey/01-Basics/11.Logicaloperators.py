# logical operators = evaluate multiple conditions ( or, and, not)
#                     or  = at least one conditions must be True 
#                     and = both conditions must be True 
#                     not = inverts the condition (not False, not True)

"""OR

temp = 25 
is_raining = True

if temp > 35 or temp < 0 or is_raining :
    print("the outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
"""

temp = 25
is_sunny = True

if temp >=28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny :
    print("It is COLD outside")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny :
    print("It is WARM outside")
    print("It is SUNNY")
"""

"""

