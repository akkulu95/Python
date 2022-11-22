""" A program that gets a list of names from the user and returns the number of names given.
"""

def number(name):
    list_of_names = names.split(",") #split the names on the basis of , and returns a list
    number_of_names = len(list_of_names)
    return number_of_names


names = input("Enter names seperated by commas (no spaces): ")
n = number(names)
print(n)