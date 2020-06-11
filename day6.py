# Day 6 - Conditionals

x = 23
print(x == 23) 
print(x == 3) 
print(x < 3) 

#Boolean

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")


statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass