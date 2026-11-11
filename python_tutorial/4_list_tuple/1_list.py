lists = ["Apple","Orange",5, 3.142, False, "Aakash", "Rohan"]

print(lists[0])
lists[0] = "Grapes" # unlikes strings lists are mutable

print(lists[0])
print(lists[1:4])

thislist = ["apple", "banana", "cherry"]
print(thislist)

# print(x := 3)  ->->-> x = 3 ; print(x)

print(list1 := ["abc",34,True, 40, "male"])

print(type(list2 := ["apple"]))

# list() constructor

thislist = list(("apple","banana"))
print(thislist)
