# update tuple 
# tuple is unchangeable so same worrkaround 
x = ("appple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x =  tuple(y)
print("1. ",x)

# Add items as same workaround
# 1. convert to list
thistuple = ("appple","banana","cherry")
y = list(thistuple)
y.append("kiwi")
thistuple = tuple(y)
print("2. ",thistuple)

# 2. add tuple to tuple
thistuple = ("appple","banana","cherry")
y = ("orange",)
thistuple += y
print("3. ",thistuple)

# Remove items as same as workaround  - can't remove directly
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print("4. ",thistuple)

# delete tuple completely by del keyword
del thistuple
# print("5. ",thistuple) # will give error