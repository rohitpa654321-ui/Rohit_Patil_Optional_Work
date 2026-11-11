print("\n1) join by + operator")
list1 = ["a","b","c"]
list2 = [1,2,3]

list3 = list1 + list2
print(list3,"\n")

print("2) join by append method")

for x in list2 :
    list1.append(x)
    list3.append(x)
print(list1,list3,"\n")

print("3) join by extend method")

list1.extend(list2)
print(list1,"\n")
