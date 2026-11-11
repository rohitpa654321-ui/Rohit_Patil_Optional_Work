thistuple = ("apple","banana","cherry")
print("1. ",thistuple[1])

# negative indexing
print("2. ",thistuple[-1])

# range of indexes
print("3. ",thistuple[1:3])
print("3. ",thistuple[-3:-1])

# check if item exists - in keyword
if "apple" in thistuple :
    print("Yes, 'apple' is in the fruits list")
