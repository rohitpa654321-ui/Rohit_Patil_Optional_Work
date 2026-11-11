# A dictionary can contain dictionaries, this is called nested dictionaries
# create a dictionary that contain three dictionaries

myfamily = {
    "child1" : {
       "name":"Yogita",
       "year": 1998
    },
    "child2" : {
        "name":"Mahesh",
        "year": 2001
    },
    "child3" : {
        "name":"Rohit",
        "year": 2005
    },

}
print("1. ",myfamily)

# Create three dictionaries, then create on edictionary that contain other three dictionaries

brother1 = {
    "name" : "Nathu Dagadu Patil",
    "work" : "Farming and tailoring"
}
brother2 = {
    "name" : "Sitaram Dagadu Patil",
    "work" : "Farming"
}
brother3 = {
    "name" : "Dnyaneshwar Patil",
    "work" : "Farming and Tailoring"
}

brothers = {
    "brother1": brother1,
    "brother2": brother2,
    "brother3": brother3
}

print("\n2. ",brothers)

# access item in nested dictionaries, use the name of dictionary, starting with the outer dictionary
# print nameof the 3 brother

print("\n3. ",brothers["brother3"]["name"])

# loop through nestd dictionaries by using iteam() method
print("\n4. ",brothers)
print("\n")
for x,obj in brothers.items():
    print(x)

    for y in obj:
        print(y+":",obj[y])
