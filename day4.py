# String Formatting

name = "Iniobong B"
print("Hello, %s!" % name)


# This prints out "John is 23 years old."
name = "John"
age = 26
print("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

data = ("Hynyobong", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s"

print(format_string % data)