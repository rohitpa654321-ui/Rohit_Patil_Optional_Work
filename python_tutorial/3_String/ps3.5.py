# Write a program to format the following letter using escape
# sequence characters.
# letter = "   Dear Rohit, this python program is amezing. Thanks!"

letter = "   \nDear Rohit,\n \tthis python program is amezing.\n \tThanks!\n"

letter =letter.replace("this","This")
print(letter)
