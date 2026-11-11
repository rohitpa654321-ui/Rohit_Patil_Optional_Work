# You can have if statements inside if statements, called nested if statements

x = 40

if x < 50 :
    print("1. x is smaller than 50")
    
    if x > 30 :
        print("x is greater than 30")
        
        if x == 40:
            print("x is equal to 40")
        
        else:
            print("try more to know no.")


# pass statement to avoid getting error if empty statement

a = 21
b = 12

if a > b :
    pass  # result as empty or blank
