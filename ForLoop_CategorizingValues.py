#Creating a mixed-type list
#Define a list with different types
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
#Use a for loop statement to traverse the list and print the data type for each item in the list
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))