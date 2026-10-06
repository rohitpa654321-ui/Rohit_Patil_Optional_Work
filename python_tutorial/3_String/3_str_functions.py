a = "hello world I am Rohit  "
b = ["hello","I am", "Rohit"]
c = "42"
print("1 : ",len(a))
print("2 : ",a.lower())
print("3 : ",a.upper())
print("4 : ",a.capitalize())
print("5 : ",a.strip())
print("6 : ",a.replace("world","python"))
print("7 : ",a.split(" "))
print("8 : ",a.find("o"))
print("9 : ",a.rfind("o"))
print("10 :",a.startswith("hello"))
print("11 :",a.endswith("hit  "))
print("12 : ",a.title())
print("13 : ",a.swapcase())
print("14 : ",a.index("I"))
print("15 : ",a.count("l"))
print("16 : ",c.zfill(5))
print("17 : ",a.center(50))
print("18 : ",a.ljust(50))
print("19 : ",a.rjust(50))
print("20 : "," ".join(b))

a ="hello"; b ="12345"; c ="hello123"; d =" "; e ="HELLO"; f ="Hello World"

print(a.isalpha())
print(b.isdigit())
print(c.isalnum())
print(d.isspace())
print(e.isupper())
print(a.islower())
print(f.istitle())

a = "\nbjhffbkhff\n"\
"vhvbdkbskhs\n"\
"vhsbsvbb" \
"  jhvb \n"
print(a)
print(a.splitlines())

#formatting :

name ="ROhit"
age ="19"
#using format()
print("\nMy name is {} and I am {} years old".format(name,age))
#using f-string
print(f"My name is {name} and I am {age} years old\n")