# keyword arguments = an argument preceded by an identifier 
#                     helps with readability 
#                     order of arguments doesn't matter
#                    1. positional 2.defult 3.KEYWORD 4.arbitrary


def get_phone(country, area , first , last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1,area=123,first=456,last=7890)

print(phone_num)


"""EX1
def hello(greeting, title , first , last ):
    print(f"{greeting} {title}{first} {last}")
# hello("Hello", "Mr.","spongebob","squarepants")
hello("Hello", title="Mr.", last="Jhon", first="James")
"""




"""EX2
for x in range(1,11):
    print(x, end=" ") # here is an keyword arguments


print("1","2","3","4","5","6",sep="-")

"""
