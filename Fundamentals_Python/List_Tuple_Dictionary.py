myFruitList = ["apple", "banana", "cherry"] #Defining a list
print(myFruitList)
print(type(myFruitList)) #Datatype is list

#Accessing a list by position i.e List's position or index will start with 0
print(myFruitList[0]) #To access the apple string
print(myFruitList[1]) #o access the banana string
print(myFruitList[2]) #To access the cherry string

#Changing the values in a list
myFruitList[2] = "orange"
print(myFruitList)

#Introducing the tuple data type
#The tuple is like a list, but it can't be changed.
#A data type that can't be changed after it's created is said to be immutable.
#you use parentheses instead of brackets ([]).
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple)) #Datatype is Tuple

#Accessing a tuple by position
print(myFinalAnswerTuple[0]) #To access the apple string
print(myFinalAnswerTuple[1]) #To access the banana string
print(myFinalAnswerTuple[2]) #To access the pineapple string

#Introducing the dictionary data type
#A dictionary is a list with named positions (keys). 
#Imagine that your list shows people’s favorite fruit.
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))


#Accessing a dictionary by name
print(myFavoriteFruitDictionary["Akua"]) #To access Akua's favorite fruit
print(myFavoriteFruitDictionary["Saanvi"]) #To access Saanvi's favorite fruit
print(myFavoriteFruitDictionary["Paulo"]) #To access paulo's favorite fruit