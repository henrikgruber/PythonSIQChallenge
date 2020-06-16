#In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. 

# Create 3 lists: numbers, strings and names
numbers = []
strings = []
names = []

# Add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")

# Add names John, Eric and Jessica to strings list
names.append("John")
names.append("Eric")
names.append("Jessica")

#Create a new variable third_name with the third name taken from names list, using the brackets operator []. Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.
third_name = names[2]

# At the end print all lists and one variable created.
print("This is the list of numbers:", numbers)
print("This is the list of strings:", strings)
print("This is the list of names:", names)
print("This is the third name in the list of names:", third_name)