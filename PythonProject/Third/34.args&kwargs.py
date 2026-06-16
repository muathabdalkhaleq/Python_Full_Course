# *args     = allows you to pass multiple non-key arguments 
# **kwrgs = allows you to pass multiple keyword-arguments 
#           * unpacking operator 
#           1. positional 2.defult 3.keyword 4.ARBITRARY

def shipping_label(*args,**kwargs):
    for arg in args:
        print (arg ,end=" ")
    print()
#    for value in kwargs.values():
#        print(value,end=" ")
#OR 2 Line
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")

    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Mr.","Muath","Ahmed","Abdalkhaleq","I",
               street = "123 Fake St.",
               pobox="PO box #100",
               #apt = "#100",
               city = "Deteoit",
               state = "MI",
               zip = "54321")

"""EX3
def print_address(**kwargs):
    #print(type(kwargs))  #<class 'dict'>
    for key, value in kwargs.items():
        print(f"{key:<8}:   {value}")

print_address(street="123 Fake St.",
              apt="100",
              city="Deteoit",
              state="MI",
              zip="54321")



"""

"""EX2
def display_name(*args):
    for arg in args:
        print(arg,end=" ")

display_name("Mr.","Muath","Ahmed","Abdalkhaleq","I")
"""

"""EX1
def add(*args):
    # print(type(args)) # tuple
    total = 0
    for arg in args:
        total += arg
    return total

print(add(10,29,31))
"""
