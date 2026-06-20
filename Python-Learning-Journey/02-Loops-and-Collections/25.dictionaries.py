# dictionary = a collection of {key:value} pairs
#              orderd and changeable . No duplicates

capitals = {"USA":"Washington D.C",
            "India":"New Delhi",
            "China":"Beiging",
            "Russia":"Moscow"}

# print(dir(capitals))
# print(help(capitals))
#print(capitals.get("USA"))

#if capitals.get("Russia"):
#    print("That capital exist")
#else:
#    print("That capitald dosen't exist")

# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
#print(capitals)



keys = capitals.keys()
print(keys)
for key in capitals.keys():
    print(key)


values = capitals.values()
print(values)
for value in capitals.values():
    print(value)

items = capitals.items()
print(items)
for key, value in capitals.items():
    print(f"{key}:{value}")