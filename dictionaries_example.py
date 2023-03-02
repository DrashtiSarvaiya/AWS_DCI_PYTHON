


# this is a list
x = ["apple", "bananas", "pear"]

x[0]  # first element
x[1]  # second element
x[2]  # ...


# this is a dictionary ---> key-value store
price_dictionary = {
    # key  : value
    "apple": 1,
    "banana": 2,
    "pear": [1, 2, 3],
    "melon": { "amount": 2, "currency": "USD" },
}
price_dictionary["apple"]


print(price_dictionary)

# S3 bucket
# object_key bucket-name/a/path/to/object/test.txt
# object_value (the object itself)

total_price = price_dictionary["apple"] + price_dictionary["banana"]

print("The price of an apple is: ", total_price)


