#Below are the two lists. Write a Python program to convert them into a dictionary in
# a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

x = dict(zip(keys, values))
print(x)

#Expected output:

#{'Ten': 10, 'Twenty': 20, 'Thirty': 30}


##Use the zip() function. This function takes two or more iterables (like list, dict, string),
# aggregates them in a tuple, and returns it.

##Or, Iterate the list using a for loop and range() function.
##In each iteration, add a new key-value pair to a dict using the update() method

#Solution 1: The zip() function and a dict() constructor

# Use the zip(keys, values) to aggregate two lists.
#Wrap the result of a zip() function into a dict() constructor.