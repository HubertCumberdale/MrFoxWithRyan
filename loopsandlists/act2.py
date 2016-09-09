from printsmooth import *


class ActTwo(object):

    def __init__(self, my_inventory):
        self.my_inventory = my_inventory
        self.act_two()

    def act_two(self):

        clear_screen()

        print_smooth('You are almost to your desk when you notice something terrifying...The most dreaded thing you can'
                     ' see in the morning. Mr. Fox is standing right at your desk waiting for you. \n\n"Come over to my'
                     ' desk," he says, "I need to review the test cases written for your last deployment."\n\nYou begin'
                     ' walking over to his desk, trailing shortly behind Mr. Fox. You know that your time is up, you '
                     'are going to have to think of something fast to avoid his wrath.')

        choices = dict(ALARM='Pull fire alarm, pretend to panic, run away downstairs and hope Mr. Fox forgets.')

        if 'COFFEE' in self.my_inventory:
            throw_coffee = 'Intentionally spill your coffee all over the floor, pretend to slip in it and flail your' \
                           ' arms around uncontrollably until Mr. Fox gets scared and runs away.'
            choices.update(COFFEE=throw_coffee)

        print_smooth('\n\nPlease enter the number of the action you would like to do.\n')

        choice_complete = False
        while not choice_complete:
            clear_screen()
            choice = user_input(self, choices)
            try:
                choice = int(choice)
            except:
                print_smooth('You must enter a number from the options given, pilgrim!')
                continue
            if int(choice) > len(choices):
                print_smooth('You must pick a number from the options given, pilgrim!')
                continue
            clear_screen()

            if choice == int(1):
                print_smooth('Mr. Fox grabs you by the neck and begins to drag you away. "If you aren\'t going to '
                             'write those test cases and think pulling a fire alarm is funny, lets see how you like'
                             ' a real burning fire!! ')
                time.sleep(2)

                print_smooth('Mr. Fox throws you down a hidden incendiary tunnel and you die.')

                time.sleep(5)
                exit()

            else:
                print_smooth('A bit of the coffee gets on to the back of Mr. Fox. Just like in the move gremlins, a'
                             ' bunch of miniature foxes begin launching from his back and attacking you. You perish, '
                             'never finishing your test cases.')
                time.sleep(5)
                exit()







