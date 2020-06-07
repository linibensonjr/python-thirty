#Lists are very similar to arrays. They can contain any type of variable, 
#and they can contain as many variables

myList = []
#use the append method to add a value to the list
myList.append(4)
myList.append(64)
myList.append(3)
myList.append(14)
myList.append(5)
print(myList[1]) #prints 64

for x in myList:
    print (x)

numbers = []
strings = []
names = ["Iniobong", "Fortune", "Joel", "Grace"]

second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

print(numbers)
print(strings)
print("The second name of the names list is %s" %second_name)