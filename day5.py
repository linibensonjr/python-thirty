# Basic String Operation

astring = "Hello World"
print (astring.index('W'))

#Slicing
print (astring[3:8])

print("Step Slicing. eg [start:end:step]")
print(astring[3:7])
print(astring[3:7:2])

#Reversing
print(astring[::-1])

print('\n'+'uppercase = '+astring.upper()+'lower case = '+astring.lower())

print(astring.startswith("Hello"))
print(astring.endswith("asd"))

print()
afewwords = astring.split(" ")
print(afewwords)
print(afewwords[1])