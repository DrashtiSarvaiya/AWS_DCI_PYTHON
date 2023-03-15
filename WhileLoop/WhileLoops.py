#Importing random and writing a while loop
#You will use the import command to include code that someone else wrote.
import random
#Working with a while loop
#A while loop makes a section of code repeat until a certain condition is met. 

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#enter a statement that will generate a random number between 1 and 10 by using the randint() function of the random module.
number = random.randint(1,10)

#Track whether the user guessed your number by creating a variable called isGuessRight
isGuessRight = False

#To handle the game logic, create a while loop
#The while loop will repeat the code inside the loop until the number is guessed correctly, which is represented by the condition isGuessRight != True in the code. 
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
 