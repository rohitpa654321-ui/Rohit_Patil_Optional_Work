# Dictionaries are used to store data values in key:value pairs and collection of ordered,
# changeable and not allow duplicates
# dictionary in python 3.7 is ordered but earlier verion have unordered
# Dictionaries are written with curly brackets, and have keys and values

# create and print dictionary and referred by using key name
# 
thisdict = {
    "brand":"Ford", # key : value 
    "model":"Mustang",
    "year" :"1964",
    "year" :"2020" # Duplicate values will overwrite existing values
}
print("1. ",thisdict)
print("2. ",thisdict["brand"]) # value print by the access by key name
print("3. ",thisdict["year"]) # overwrite existing value

print("4. ",len(thisdict)) # len() function to dertermine the length of dictionary

# Data types
# string, int, boolean, and list data types:
thisdict = {
    "brand"    : "Ford",
    "electric" : False,
    "year"     : 1964,
    "colors"   : ["red","yellow","black","grey","white"]
}
print("6. ",thisdict)
print("5. ",type(thisdict))

# dict() constructor to create dictionary
thisdict = dict(name = "rohit", age = 20, country = "India")
print("7. ",thisdict)
 