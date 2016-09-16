from printsmooth import *


def act_two(self):

    clear_screen()

    print_smooth('You are almost to your desk when you notice something terrifying...\n\nThe most dreaded thing you can'
                 ' see in the morning. \n\nMr. Fox is standing right at your desk waiting for you. \n\n"Come over to my'
                 ' desk, ' + self.name + '," he says. \n"I need to review the test cases written for your last '
                 'deployment."\n\n')

    raw_input('Press enter to follow Mr. Fox.')
    clear_screen()
    laptop_q = user_input(self, "Do you take your laptop with you, yes or no?\n\n")
    if "n".upper() in laptop_q.upper():
        print_smooth('"Maybe if I dont bring my laptop he won\'t really make me show him." you\nthink to yourself.')
        self.my_inventory.remove("LAPTOP")
    else:
        print_smooth("You grab your laptop and try not to hyperventilate.\n\n")

    print_smooth('You begin walking over to his desk, trailing shortly behind Mr. Fox. \n\nYou know that your time is '
                 'up, you are going to have to \nthink of something fast to avoid his wrath.')

    choices = dict(ALARM='Pull fire alarm, pretend to panic, run away downstairs and hope Mr. Fox forgets.')

    if 'COFFEE' in self.my_inventory:
        self.my_inventory.remove("COFFEE")
        throw_coffee = ('Intentionally spill your coffee all over the floor, pretend to slip in it and \nflail your '
                        'arms around uncontrollably until Mr. Fox gets scared and runs away.')
        choices.update(COFFEE=throw_coffee)

    if "LAPTOP" in self.my_inventory:
        detonate_laptop = ("You remember that the battery in your laptop has a recall due to \nexploding under "
                           "pressure. \n\nYou could smash it in hopes that it causes a distraction so you can escape.")

        choices.update(LAPTOP=detonate_laptop)

    print_smooth('\n\nYou arrive at his desk. Please select the key word of the action you would like to perform.\n')

    choice_complete = False
    while not choice_complete:
        choice = user_input(self, choices).upper()
        if choice not in choices:
            print_smooth('You must enter a choice from the options given, pilgrim!')
            clear_screen()
            continue

        if choice == 'ALARM':
            clear_screen()
            print_smooth('Mr. Fox grabs you by the neck and begins to drag you away. \n\n"If you aren\'t going to '
                         'write those test cases and think pulling \na fire alarm is funny, lets see how you like'
                         ' a real burning fire!! ')
            time.sleep(2)

            print_smooth('Mr. Fox throws you down a hidden incendiary tunnel and you die.')

            time.sleep(5)
            exit()

        elif choice == 'COFFEE':
            clear_screen()
            print_smooth('A bit of the coffee gets on to the back of Mr. Fox. \n\nJust like in the movie gremlins, a'
                         ' bunch of miniature foxes begin \nlaunching from his back and attacking you. \n\nYou perish, '
                         'never finishing your test cases.')
            time.sleep(5)
            exit()

        elif choice =="LAPTOP":
            clear_screen()
            print_smooth("You smash the laptop to the ground, while jumping back several steps,\nlike a ninja with a "
                         "smoke bomb. \n\nThe battery does not explode... the recall was for that android phone, not "
                         "your laptop, dummy. \n\nYou stand still as everyone else laughs...\n\nMr. Fox isn't laughing."
                         "\n\nHe picks up the flopping laptop and bludgeons you to death with it. \n\nEveryone else "
                         "continues to laugh.")
            time.sleep(5)
            exit()

        else:
            clear_screen()
            print_smooth('well...you lose. whatever.')
            time.sleep(5)
            exit()







