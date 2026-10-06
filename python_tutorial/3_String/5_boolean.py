# Boolean function use as compare

print(10 > 9)
print(10 == 9)
print(10 < 9)

#Boolean in an if statement

a = 200
b = 33

if b > a:
    print("\nb is greater than a\n")
else:
    print("\nb is not greater than a\n")

# Evalute value and variables 'bool()' function is used

print(bool("\nHello"))
print(bool(15,),"\n")

#  Some Values are False
# (),[],{},"",0,None, False

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}),"\n")

# Funnction can Return a Boolean

def myFunction():
    return True
if myFunction():
    print("YES!\n")
else:
    print("No!\n")

# isinstance() function is used to determine object
# is of a certain data type

x = 2300.00
print(isinstance(x,int))
print(isinstance(x,float))
print(isinstance(x,str),"\n")