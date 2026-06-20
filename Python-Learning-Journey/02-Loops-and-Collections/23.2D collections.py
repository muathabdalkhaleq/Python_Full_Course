
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
    
# fruits =     ["apple","orange", "banana","coconut"]
# vegetables = ["celery","carrots","potatoes"]
# meats =      ["chiken","fish","turkey"]

# geroceries = [fruits, vegetables, meats]

# print(geroceries[0][0])

geroceries = [["apple","orange", "banana","coconut"],
              ["celery","carrots","potatoes"],
              ["chiken","fish","turkey"]]

#print(geroceries[0][0])

for collection in geroceries:
    for food in collection:
        print(food,end=" ")
    print()

    