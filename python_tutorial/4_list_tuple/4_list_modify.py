print("1) To insert item at end of the list\n")
lists = ["Apple","Orange",5, 3.142, False, "Tea", "mango"]
print(lists)
lists.append("Sugar")
print(lists)

print("\n2) TO insert item to the indexes as needed\n")
thislist = ["apple","banana","cherry"]
thislist.insert(2,"mango")
thislist.insert(2,"mango")
print(thislist)

print("\n3) Extend list : append items from another list\n")
thislist = ["apple","banana","cherry"]
tropical = ["mongo","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)

print("\n4) Remove list items :remove()\n")
thislist = ["apple","banana","cherry","banana"]
thislist.remove("banana") # only removes first occurence
print(thislist)

print("\n5) remove specified index : pop()")
thislist = ["apple","banana","cherry","banana","mango"]
thislist.pop(1) # if you do not specify index, pop()
print(thislist) # method removes the last item of the list.

print("\ndel keyword also removes the specified index:\n")
thislist = ["apple","banana","cherry"]
del thislist[0] # the del can delete the list completely.
# del thislist
print(thislist) # give erroe because list is completely delete

print("\n6) Clear the list : clear()\n")

thislist = ["apple","banana","cherry"]
thislist.clear()
print(thislist)

l1 = [1,34,56,2,41,3,56,13,75]
print(l1)
l1.sort()
print(l1)