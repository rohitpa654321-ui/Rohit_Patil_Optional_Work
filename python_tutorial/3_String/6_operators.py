print("Python Operators")

print("1) Arithmetic operators")

x = 2 ; y = 5

print(x + y) # Addition
print(x - y) # Suntraction
print(x * y) # Multiplication
print(x / y) # Division
print(y % x) # Modulus (return remainder)
print(x ** y) # Exponentiation (return a to the power b)
print(y // x,"\n") # Floor Division (rounds the result down to the
               # nearest whole number)

print(pow(x,y),"\n") # (Extra part) pow() function is used as x power y


print(" 2) Python Assignment Operators\n")


x = 5 ; print(x) # x = 5
x += 3 ; print(x) # x = x + 3
x -= 4 ; print(x) # x = x - 4
x *= 5 ; print(x) # x = x * 5
x /= 1 ; print(x) # x = x / 1
x %= 9; print(x) # x = x % 9
x *= 8
x //= 2 ; print(x) # x = x // 2
x **= 2 ; print(x) # x = x ** 2
x=5
x &= 3 ; print(x) # x = x & 3
x |= 3 ; print(x) # x = x | 3
x ^= 2 ; print(x) # x = x ^ 2
x >>= 2 ; print(x) # x = x >> 2
x <<= 2 ; print(x) # x = x << 2
print(x := 3)  # x = 3 ; print(x)


print("\n3) Python Comparison Operators :\n")

x = 5 ; y = 5

print (x == y) # Equal
print (x != y) # Not equal
print (x > y) # Greater than
print (x < y) # Less than
print (x >= y) # Greater than or equal to
print(x <= y) # Less than or equal to

print("\n4) Python Logical operators :\n")
x = 5
print(x > 3 and x < 10)# and returns True if one statement is true
print(x > 3 or x > 10) # or returns True if both statements are true
print (not(x > 3 or x < 10)) # not reverse the result, returns False if the result is true

print("\n5) Python Identity Operators :\n")
print("a) is :\n")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # returns True because z is the same object as x
print(x is y)# returns False because x is not the same object as y, even if they have the same content
print(x == y)# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print("\nb) is not :\n")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)# returns False because z is the same object as x
print(x is not y)# returns True because x is not the same object as y, even if they have the same content
print(x != y)# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

print("\n6) Python Membership Operators :\n")
print("a) in :")
x = ["apple", "banana"]

print("banana" in x)# returns True because a sequence with the value "banana" is in the list

print("\nb) not in :")

x = ["apple", "banana"]
print("pineapple" not in x)# returns True because a sequence with the value "pineapple" is not in the list

print("\n7) Python Bitwise Operators\n")

print(6 & 3) # It gives 2 because 110(6) & 11(3)
# value 1 & 1 will give 1 and 1 & 0 give 0 
# Final 10(2)
print(6 | 3) # It gives 7 because 110(6) or 11(3)
# 1 or 1 = 1, 1 or 0 = 1, 0 or 0 = 0
# Final 111(7)
print(6 ^ 3) # output 5 because ^(XOR)
# 110 ^ 11 = 101 (campare each bit and set 1 if only one is 1 otherwise if both are 1 or 0 it is set to 0.
print(~ 3 ) # output -4 because inverts all the bits
# 0000000000000011(3) , 1111111111111100(-4)
print( 3<< 2) # Shift left by pushing zeros in from the right and let the leftmost bits fall off
# 0011(3) will be 1100(12)
print(8 >> 2) # Operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's
# 1000(8) = = 0010 (2)