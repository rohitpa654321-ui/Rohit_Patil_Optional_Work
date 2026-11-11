print("1) Access Item by indexes\n")

thislist = ["apple","banana","cherry"]
print(thislist[1]) # apple at 0 index and banana at 1 index

print("\n3) Negative indexing\n")

print(thislist[-1])

print("\n 4) Range of indexes\n")
thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])

print("\n5) Range of Negative Indexes\n")

print(thislist[-4:-1])
print(thislist[-4: ])

print("\n6) Check if Item exist\n")

if "apple" in thislist:
    print("Yes!, 'apple' is in the list is present\n")
