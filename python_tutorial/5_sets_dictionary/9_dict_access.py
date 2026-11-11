# Access the items of a dictionary by referring to its key name, inside square brackets:
# get() method also gives same result

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964
}
print("1. ",thisdict["model"])
print("2. ",thisdict.get("model"))

# keys() method, returns all keys list in dictionary
# any changes done to the dictionary will be reflected in the keys list.
x = thisdict.keys()
print("\n3. ",x) # before change
thisdict["year"] = 2025
thisdict["color"] = "white"
print("4. ",x) # After change

# values() a method will return a list of values in dictionarys
# changes will reflect
x = thisdict.values()
print("\n5. ",x)
thisdict["year"] = 2020
thisdict["color"] = "grey"
thisdict["electric"] = False
print("6. ",x)

# items() method return each item in a dictionary, as tuple in a list
# changes will reflect
x = thisdict.items()
print("\n7. ",x) # before changes

thisdict["color"] = "red"
print("\n8. ",thisdict)

del thisdict["electric"]
print("9. ",thisdict)

thisdict["colors in"] = ["white","grey","red","yellow"]
print("10.  ",thisdict)

thisdict["average"] = "7KM"
print("\n11. ",x) # after changes

# check if key exists by use in keyword
print("\n12. ",thisdict)
if "average" in thisdict:
    print("13. Yes,'average' is given in thisdict dictionary ")
