from loopsandlists.printsmooth import *

clear_screen()
print_smooth("You enter a dark room with two doors.  Do you go through door #1 or door #2?")

door = raw_input("\n\n>>> ")
clear_screen()

if door == "1":
    print_smooth("There's a giant bear here eating a cheese cake.  What do you do?")
    print_smooth("\n1. Take the cake.")
    print_smooth("\n2. Scream at the bear.")

    bear = raw_input("\n\n>>> ")
    clear_screen()

    if bear == "1":
        print_smooth("The bear eats your face off.  Good job!")
    elif bear == "2":
        print_smooth("The bear eats your legs off.  Good job!")
    else:
        print_smooth("Well, doing %s is probably better.  Bear runs away." % bear)

elif door == "2":
    print_smooth("You stare into the endless abyss at Cthulhu's retina.")
    print_smooth("\n1. Blueberries.")
    print_smooth("\n2. Yellow jacket clothespins.")
    print_smooth("\n3. Understanding revolvers yelling melodies.")

    insanity = raw_input("\n\nWhat would you like to choose? >>>")

    clear_screen()

    if insanity == "1" or insanity == "2":
        print_smooth("Your body survives powered by a mind of jello.  Good job!")
    else:
        print_smooth("The insanity rots your eyes into a pool of muck.  Good job!")

else:
    clear_screen()
    print_smooth("You stumble around and fall on a knife and die.  Good job!")


