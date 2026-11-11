# several ways to remove the items

# 1. pop(), method removes item with specific key name
# 2. popitem(), method remove last inserted item
# 3. clear() ,method empties the dictionary
# 4. del , keyword delete item , can also delete dictionary completely

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964 ,
    "color" : "grey",
    "average" : "7KM"

}
thisdict.pop("color")
print("1. ",thisdict)
thisdict.popitem()
print("2. ",thisdict)
del thisdict["year"]
print("3. ",thisdict)
thisdict.clear()
print("4. ",thisdict)
del thisdict
# print(thisdict) # give error because thisdict is n longer exists
