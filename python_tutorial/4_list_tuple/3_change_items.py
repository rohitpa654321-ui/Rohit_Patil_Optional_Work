print("1) change item value\n")

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist[1] = "blackberry"
print(thislist) ; print(len(thislist))
print("\n")

thislist[2:5] =["watermelon","pinapple","stawberry","berry"] # 2,3,4 indexes change the value and berry added
print(thislist) ; print(len(thislist))                       # because berry is more than the required
print("\n")

thislist[2:5] = ["banana"] # 2 index value change and 3,4 index will be replace as null and remaining will take place according.
print(thislist) ; print(len(thislist))
