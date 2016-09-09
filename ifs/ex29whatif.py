# "=" assigns a value. For instance:
# x = 2
# print x
#
# # printing x shows 2 because we have assigned x to the value 2.
#
# # "==" evaluates the values of objects. So if we say x == 2 it will
# # return us a boolean of True or False.
#
# print x == 2
# print x == 3
#
#












people = 20
cats = 30
dogs = 15


# if people < cats: # only executes if people is less than cats
#     print "Too many cats! The world is doomed!"
#
# if people > cats: # only executes if people is greater than cats
#     print "Not many cats! The world is saved!"
#
# if people < dogs:
#     print "The world is drooled on!"
#
# if people > dogs:
#     print "The world is dry!"



dogs += 5 # This is shorthand for dogs = dogs + 5

if people > dogs:
    print "People are greater than or equal to dogs."

if people < dogs:
    print "People are less than or equal to dogs."


if people == dogs:
    print "People are dogs."