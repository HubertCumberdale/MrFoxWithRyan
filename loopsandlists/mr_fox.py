from printsmooth import *
from act2 import *


class MrFox(object):

    def __init__(self):
        self.my_inventory = ['LAPTOP']
        self.name = ''

    def act_one(self):
        clear_screen()
        print_smooth("Welcome to my story about an evil Fox. \n\n\n\nCopyright Adam Mower & Ryan Throckmorton."
                     "\n\nAt any time during this story you can enter 'INV' to check your inventory.\n\n")
        time.sleep(.5)
        raw_input('Press any key to continue')
        clear_screen()

        self.name = user_input(self, "Please, tell me your name.\n\n")
        if self.name.upper() == "JEREMIAH":
            print 'Get out of my program!!!'
            exit()

        print_smooth('Great! Thank you ' + self.name + '!')

        sex = user_input(self, "Are you a male or a female? \n\n")

        if 'f' in sex.lower():
            sex = 'FEMALE'
            print_smooth("Thank you Ma'am.")
        else:
            sex = "MALE"
            print_smooth("Thank you Sir.")

        clear_screen()

        print_smooth('It was a pleasant, fall morning. You come to work bubbling with anticipation for what the day '
                     'will bring. You know that you have written only a few test cases the entire last quarter of work '
                     'though. Today...today is the day you write those damn test cases.')

        print_smooth('\n\nYou walk through the cafeteria into work. Do you grab yourself a coffee? Yes or No?')

        coffee = user_input(self)

        if 'y' in coffee.lower():
            self.my_inventory.append('COFFEE')
            print_smooth("\nYou pour yourself a warm cup o'joe and head upstairs. ")
        elif 'n' in coffee.lower():
            print_smooth('\n"You are a strong, independent ' + sex.lower() + " who don't need no stinkin' coffee!"
                         " You head upstairs to begin work. ")

        time.sleep(1.5)

        return act_two(self)

start = MrFox()

start.act_one()
