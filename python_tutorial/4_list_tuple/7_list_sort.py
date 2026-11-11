print("\n1) sort alphabetically")
thislist = ["orange","mango","89","kiwi","2","8"]
thislist.sort()
print(thislist,"\n")

print("2) sort numerically")
thislist = [23,12,21,76,34,26.89,2]
thislist.sort()
print(thislist,"\n")

print("3) Reverse sort")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist,"\n")

print("4) Case Insensitive sort: capital case come first")
thislist = ["banana", "Orange","23", "Kiwi", "cherry"]
thislist.sort()
print(thislist,"\n")

print("5) If Lower wants first")
thislist = ["banana", "Orange","23", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist,"\n")


print("6) Reverse")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) 