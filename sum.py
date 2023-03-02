

# Enter numbers: 10, 20, 30
# Result is: sum of all numbers
print("Enter numbers: ", end="")
numbers_input = input()

#"10, 20, 30" # make string to list of integer 
#[10,20,30] 

split_numbers = numbers_input.split(",") # "10, 20, 30" --> ["10", "20", "30"]

# We could write this, but its tedious :( 
# 
# first_number = split_numbers[0]
# first_number_stripped = first_number.strip() # strip() remove any whitespaces from the start and the end
# n1 = int(first_number_stripped)

# second_number = split_numbers[1]
# second_number_stripped = second_number.strip() # strip() remove any whitespaces from the start and the end
# n2 = int(second_number_stripped)


# A loop will make it more dynamic and easier to write
result = 0
for number in split_numbers:
    xi = int(number.strip())
    result = result + xi
    print("current result =", result)


print("the input was: ", result)