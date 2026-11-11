# List methods

# 1. add() method , add element to set
syntax: set.add("element")
# . remove() method, remove element from set
syntax: set.remove("element")
# . discard() method, remove element from set
syntax: set.discard("banana")
# pop() method, remove element from set but specifically don't known that which is removed
set.pop()  # to see which is removed : x = set.pop() ; print(x)
# . clear() method
syntax: set.clear()
# . copy() method
syntax: set = set1.copy()

# union() method returns a set containing the union of sets
syntax: set = set1.union(set2,list1,tuple1,...)
# instead union() can use | operator (or) for set with set
syntax: set = set1 | set2 | set3...

# update() method, update the set with the union of this set and others
syntax: set.update(set1,list1,tuple1,...)
# instead update() can use |= operator for set with set
syntax: set |= set1 | set2 | set3

# difference() method, Return a set that contains the items that only exist in set x, and not in set y,z,..
syntax: set = set1.difference(set2,list1,tuple1,...)
# instead difference() can use - operator for set with set
syntax: set = set1 - set2 - set3...
# difference_update(), same as above, but changes can done in current set no need of new set
syntax: set.difference_update(set1,list1,tuple2,...)
# instead difference_update() can use -= operator for set with set
syntax: set -= set1 | set2 | set3...

# intersection() method, returns elements(intersection) present in both set or common
syntax: set = set1.intersection(set2,list1,tuple1,...)
# instead intersection() can use & operator for set with set
syntax: set = set1 & set2 & set3...
# intersection_update() method, as above, but changes can done in current set no need of new set
syntax: set.intersection_update(set1,list2,tuple1...)
# instead intersection_update() can use &= operator for set with set
syntax: set &= set1 & set2 & set3...

# symmetric difference() method, returns the elements are not common in sets
syntax: set.symmetric_difference(set1)
# instead symmetric_difference() can use ^ operator for set with set
syntax: set ^ set1
# symmetric_difference_update() method, as above, but changes done in current set
syntax: set.symmetric_difference_update(set1)
# instead symmetric_difference_update() can use ^= operator for set with set
syntax: set ^= set1