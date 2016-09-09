# for loops iterate over items in a sequence such as alist!

x = 'Heywhatsuphello'

my_sweet_list = [1, 2, 3, 4, 5, 'hi', x, 'hello']

for i in my_sweet_list:
    print i

# Adding some logic
for number in my_sweet_list:
    if type(number) == int:
        print "Hi number {}!".format(number)

# same as above
for string in my_sweet_list:
    if type(string) == str:
        print 'The list string is "{}".'.format(string)








# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

