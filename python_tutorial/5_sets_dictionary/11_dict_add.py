# adding items to the dictionary
# by key names or update() method
thisdict ={
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964
}

thisdict["color"] = "grey"
thisdict.update({"average":"7KM"})

print(thisdict)