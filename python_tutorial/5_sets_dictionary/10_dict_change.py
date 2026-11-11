# change specific value by reffering to its key name
# or by update method 
thisdict = {
    "brand" : "Ford",
    "model" : "mustang",
    "year"  : "2020",
    "color" : "grey"
}
thisdict["year"] = 1964 # by using key name
thisdict.update({"color":"red"}) #change by update() method

print(thisdict)