# https://learnpythonthehardway.org/book/ex32.html

# The list is a most versatile datatype available in Python which can be written as a list of comma-separated values
# (items) between square brackets. Important thing about a list is that items in a list need not be of the same type.
# The list type is a container that holds a number of other objects, in a given order. The list type implements
# the sequence protocol, and also allows you to add and remove objects from the sequence.

x = 'Heywhatsuphello'

my_sweet_list = [1, 2, 3, 4, 5, 'hi', x, 'hello']

print my_sweet_list


# Adding, deleting, rearranging values

y = 400

my_sweet_list.append(y)  # Appends item to end of list.
print my_sweet_list

my_sweet_list.insert(0, 'start of list!')  # inserts item at index #.
print my_sweet_list

my_sweet_list.pop()  # Removes the last item in a list
print my_sweet_list

my_sweet_list.remove(x)
print my_sweet_list

my_sweet_list.sort()

print my_sweet_list

