# match statement select one of many code blocks to be executed
# match statement is same as switch condition in C.

day = 4  # input from the user

match day:
    case 1 :
        print("monday")
    case 2 :
        print("tuesday")
    case 3 : 
        print("wednesday")
    case 4 :
        print("thusday")
    case 5 :
        print("friday")
    case 6 :
        print("saturday")
    case 7 :
        print("sunday")

# default value or case: use the underscore _ for if you want to execute when there is no matches
# the value _ always match
    case _ :
        print("No match")

# | pipe character to combine value an or operator in case to check more than one value match in one case
#  if statement is used as extra condition check
print("\n")
month = 5
day = 4

match day:
    case 1 | 2| 3 | 4 | 5 if month == 4 :
        print("A weekday of April")
    case 1 | 2 | 3 | 4 | 5 if month == 5 : 
        print("A weekday of May")
    case _ :
        print("No match")