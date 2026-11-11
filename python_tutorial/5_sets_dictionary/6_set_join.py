# several ways to join sets

# union() method set with any iteration and return new set: syntax : set=set1.union(set2,set3,..)
# | operator can be use instead union(), but only set with set : syntax : set = set1 | set2 | set3 | ...
set1 = {"apple","banana","cherry"}
list1 = (1,2,3,3)
set2 = {"a","b","c"}
set = set1.union(list1,set2)
x = {"apple","banana","cherry"}
y = {1,2,3,3}
z = {"a","b","c"}
myset = x|y|z

print("1. ",set)
print("2. ",myset)

# update() method used to make change in current set with any iteration
set1 = {"apple","banana","cherry"}
list1 = (1,2,3,)
set1.update(list1)
print("\n3. ",set1)

# intersection() method return new set contain common iteams in both set with any iteration
#  & operator can be used instead of intersection(), but only allows set with set
set1 = {"apple","you","banana"}
list1 = ("me","you","banana")
set = set1.intersection(list1)
x = {"apple","banana","you"}
y = {"me","you","banana"}
z = x & y
print("\n4. ",set)
print("5. ",z)

# intersection_update() change current set with any interation
# &= operator can used instead above, but only set with set : syntax : set &= set1 & set2 & set3...
set1 = {"apple","you","cherry"}
list1 = ("me","you","apple")
set1.intersection_update(list1)

print("\n6. ",set1)

# True ,False / 1, 0  considered as duplicates
set1 = {"apple","1","banana","0","cherry"}
set2 = {"False","google","apple",2,"True"}
set = set1.intersection(set2)
print("\n7. ",set)

# difference() method returns new set contains only items from set1 is not present in any iteration(set2,list1,tuple1)
# - operator (minus) can used instead difference(), but allows set with set: syntax: set = set1-set2
set1 = {"apple","you","cherry"}
list1 = ("me","you","apple")
set = set1.difference(list1)
print("\n8. ",set)

# difference_update() as above but change in current set
# -= operator instead above : syntax: set1-=set
set1 = {"apple","you","cherry"}
list1 = ("me","you","apple")
set1.difference_update(list1)
print("9. ",set1)

# symmetric_difference() method, new set contain iteams not common in both sets
# ^ operator can be used instead of above: syntax: set = set1 ^ set2 
set1 = {"apple","you","cherry"}
set2 = ("me","you","apple")
set = set1.symmetric_difference(set2)
print("\n10. ",set)

# symmetric_difference_update() method as above but change in current set
# ^= operator can be used instead of above: syntax: set1 ^= set2
set1 = {"apple","you","cherry"}
set2 = ("me","you","apple")
set1.symmetric_difference_update(set2)
print("11. ",set)

