people = 20
cars = 10
trucks = 15

# The if, each elif (contraction of "else if"), and the final else line are all aligned. 
# There can be any number of elif lines, each followed by an indented block. 
# With this construction exactly one of the indented blocks is executed. 
# It is the one corresponding to the FIRST True condition, or, if all conditions are False, 
# it is the block after the final else line.



# if cars < people:
#     print 'hi'
#
# elif cars < people:
#     print "We should not take the cars."
#
# else:
#     print "We can't decide."




if not trucks:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."



#



#
# if people == trucks:
#     print "Alright, let's just take the trucks."
# else:
#     print "Fine, let's stay home then."
