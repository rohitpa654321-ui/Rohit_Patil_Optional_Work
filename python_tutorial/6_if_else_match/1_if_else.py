# Python condition

# 1. equals : a == b
# 2. not equals : a != b
# 3. less than : a < b
# 4. less than and equal to : a <= b
# 5. greater than : a > b
# 6. greater than and equal to : a >= b

# 1. if statement : if
# most conditions commonly used in "if statement" and loop
# 2. elif statement : elif 
# if previous condition were not true, then try this condition
# 3. else statement : else
# do this if certain conditions are not true or fails
# you can also have an else without the elif 

a = 21
b = 201

if a > b :
    print("1. 'a' is greater than 'b'")
elif a == b :
    print("1. 'a' is equal to 'b'")
else:
    print("1. 'b' is greater than 'a'")


# short hand if
if a < b : print("\n2. 'b' is greater than a")

# short hand if...else
print("\n3. A") if a > b else print("3. \nB")

# one line if else statement with 3 condition
a = 21
b = 21

print("\n4. A") if a > b else print("4. \n=") if a == b else print("4. \nB")

# and, or ,not keyword

a = 21
b = 32
c = 43

if a < b and b < c :
    print("\n5. Both conditions are true")
if a > b or c > b :
    print("6. Atleast one condition is true")
if not b > a :
    print("7. b is not greater than a")

