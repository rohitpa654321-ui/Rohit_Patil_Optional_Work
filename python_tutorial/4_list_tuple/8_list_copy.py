print("\n1) copying list by copy method")
thislist = ["apple","banana","cherry"]
mylist = thislist.copy()
print(mylist,"\n")

print("2) copying list by list method")
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist,"\n")

print("2) copying list by slice (:) operator")
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist,"\n")
