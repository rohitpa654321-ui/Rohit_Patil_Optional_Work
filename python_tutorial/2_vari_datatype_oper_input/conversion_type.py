
x = 1    # int
y = 2.8  # float
z = 6+4j   # complex

# int to float:
a = float(x)
 #float to int:
b = int(y)
# int to complex:
c = complex(x)
# flaot to complex:
d = complex(y)

# Note : complex have 2 parts
#       real and imaginary you have chose
#       which you want to convert by appying
#       .real or .imag to the end of variable

# complex to int
e = int(z.real)
f = int(z.imag)
# complex to float
g = float(z.real)
h = float(z.imag)



print("a=x=",a)
print("b=y=",b)
print("c=x",c)
print("d=y",d)
print("e=z",e)
print("f=z",f)
print("g=z",g)
print("h=z",h)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))