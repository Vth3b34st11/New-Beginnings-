# We use while loops to repeat a line of code multiple times
# First declare a variable (here it is "V")
V = 1
while V <= 10:
    print(V)
    V = V + 1
# Using the multiplication operator we can multiply a number by a string
# Moving onto lists (use square brackets to represent list)
names = ["Cahil", "Terry", "Luiz", "James", "Caesar"]
names[0] = "Cahila"
print(names)
print(names[0])
print(names[4])
print(names[0:2])
# colon would only select the range up to the end value (not the end value)
numbers = [1,2,3,4,5,6,7,8,9,10]
numbers.insert(0,-1)
# numbers.append adds a value at the end of the existing list
numbers.remove(5)
print(numbers)
print(20 in numbers)
# Boolean operator "in" to check for number in list
print(len(numbers))
# printing "len" of the object provides the number of values in our list

for item in numbers:
    print(item)
# For loops make the code shorter than while loops using a loop variable "item" to print all values separately
# A tuple is a non-modifiable list where normal brackets are used instead of square brackets


