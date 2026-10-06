# Write a program to fill in a letter template
# given below with name and date

letter = '''
        Dear <|Name|>,
                    You are selecated !
                    <|Date|>
                    '''
print(letter.replace("<|Name|>","Rohit").replace("<|Date|>","21 march 2028"))