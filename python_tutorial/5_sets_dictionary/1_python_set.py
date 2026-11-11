# Note: sets are unchangeable, but you can remove and add new items.
# Note: sets are unordered, so you cannot be sure in which order items will appear.
# Note: The value True and 1 / False and 0 are considered as same value in set, and treated as duplicates.

# create a set
thisset = {"Me","Love","You"}
print("1. ",thisset) # unordered : refresh or rerun for see changes

# duplicates not allowed
thisset = {"apple","banana","apple","cherry","banana"}
print("2. ",thisset) # same value considered as one value

# True and 1 / False and 0 are considered as same value and treated as duplicate
# The value which comes first will considered from both
thisset = {1,True,"apple",False,"banana",0}
print("3. ",thisset)

# length of set:  len()
print("4. ",len(thisset))

# Data type
set1 = {"apple","banana","cherry"}
set2 = {1,32,21,43}
set3 = {True, False,True}
set4 = {"abc","32",True,21,"male"}
# type()  function
print("5. ",type(set4))

# set()  constructor
thisset = set(("apple","banana","cherry")) # Note: double round brackets
print(thisset)