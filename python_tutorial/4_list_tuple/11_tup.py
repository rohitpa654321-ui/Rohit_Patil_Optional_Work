# Tuple with round brackets
tup1 = (1,2,3,4,5)
print("1. ",tup1)

# access tuple items
print("2. ",tup1[2])
print("3. ",tup1[2:3])
print("4. ",tup1[0:3])

# valid tuple
tup2 = (1) # Not a tuple
tup3 = (1,) # Tuple with single element
tup4 = ("abc",34,True,40,"male") # Tuple

# Data type 
print("5. ",type(tup2))
print("6. ",type(tup3))
print("7. ",type(tup4))

# tuple length
print("8. ",len(tup4))

# tuple()  -Constructor
thistuple = tuple(("apple","banana","cherry")) # note double round brackets
print("9. ",thistuple)

