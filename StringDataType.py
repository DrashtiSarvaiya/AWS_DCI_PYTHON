myString = "This is a string."
print(myString)
print(type(myString)) #String Datatype
print(myString + " is of the data type " + str(type(myString)))
 
#Working with string concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#Working with input strings
name = input("What is your name? ") #input() = User can give any name or input here
print(name)

#Formatting output strings
color = input("What is your favorite color?  ")
print(color)
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))