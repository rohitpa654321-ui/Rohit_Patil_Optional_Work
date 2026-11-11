list1 = ["a","b","c"]
list4 = ["b","c","a"]
list2 = [1,2,3]
list3 = []

# 1) append()   add element in end
list1.append(list2)
print("1. ",list1)

# 2) copy()  returns copy of list
list1 = list2.copy()
print("2. ",list1)

# 3) extend()  add elements from any iteration
list1.extend(list4)
print("3. ",list1)

# 4) count()  returns no. of elements
print("4. ",list1.count("a"))

# 5) index() return index of element
print("5. ",list1.index("c"))

# 6) insert() add element at specified position
list1.insert(4,6)
print("6. ",list1)

# 7) pop()  remove element from specified position
list1.pop(4)
print("7. ",list1)

# 8) remove()  remove item with the specified value
list1.remove(3)
print(list1)

# 9) reverse() reverse th order of list
list1.reverse()
print(list1)

# 10) sort()  sort the list if all elements are alpha or num
list4.sort()
print(list4)

# 11) clear()  removes all elements
list1.clear()
print(list1)