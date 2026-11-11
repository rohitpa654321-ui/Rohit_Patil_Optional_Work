print("loop through a list") # loop list items by using a for loop
print("\nUsing for loop\n")

thislist = ["apple","banana","cherry"]
for x in thislist:
    print(x)

print("\nThrough the index number: range() and len()\n")

thislist = ["apple","banana","cherry"]
for i in range(len(thislist)):
    print(thislist[i])

print("\nusing while loop : while loop and len()\n")

thislist = ["apple","banana","cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

