# \n is used for new line
# \t is used to give tabspace
# \"boy\" here \ is used to locate string start-end with in the string

a = "\nRohit is a good boy\nbut not \t a bad \"boy\"\n"

print(a)
# \\ output : "\"
# \' output : '
# \" output : "
# \t output : " "
b = "your\' name\" is\t rakoo \\"
print(b)

# \r from we use above character replace on front characters untill ends and remaining remains as it is.
c = "I am Ghansyam i\rPatil\n"
print(c)

# \b backspace it delete or remove single back character
# \f new paragraph
# \v vertical tab space

d = "we\f are \v\vfriend\b\bs"
print(d)

# \0 is null character which is invisible 
print("null\0\0char")