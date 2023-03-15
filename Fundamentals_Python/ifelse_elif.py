# Working with the if statement
#Use the input() function to get information from the user
userReply = input("Do you need to ship a package? (Enter yes or no) ")

#Use the if-else statement to print a response.
if userReply == "yes": #The == symbol is a comparative operator. It means is equal to.
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
    
#Working with the elif statement
#The elif statement always comes after an if statement and before the else statement.
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
