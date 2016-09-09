import time

#  A while-loop will keep executing the code block under it as long as a boolean expression is True.
# What they do is simply do a test like an if-statement, but instead of running the code block once,
# they jump back to the "top" where the while is, and repeat. A while-loop runs until the expression is False.

# count = 0
# while (count < 9):
#    print 'The count is:', count
#    count = count + 1
#    time.sleep(1)
#
# print "Good bye!"

# Be careful when using while loops to not make a loop that does not end. For example:

# count = 0
# while (count < 9):
#    print 'The count is:', count
#    time.sleep(1)
#
# print "Good bye!"
#
# #   ^
# #   |
# #   |
# #   |
#
# # The expression in this while loop will never evaluate to False, so the while loop would run forever.
#
