# Note: set is unordered, by pop() don't know which iteam that gets removed

# Remove iteam by remove() or discard() method
set = {"apple","banana","cherry","kiwi"}
set.remove("banana")
print("1. ",set)
set.discard("kiwi")
print("2. ",set)

# remove random iteam use pop() method
set1 = {"apple","banana","cherry"}
x = set1.pop() # x store removed value
print("\n3. ",x) # will show pop iteam
print("4. ",set1)

# clear the set use clear() method
set1 = {"apple","banana","cherry"}
set1.clear()
print("\n5. ",set1)

# to delete set use del keyword
set1 = {"apple","banana","cherry"}
del set1
print(set1) # error because set1 is no longer exists
