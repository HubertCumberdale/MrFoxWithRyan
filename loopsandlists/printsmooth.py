import os
from sys import stdout
import time


def clear_screen():
    os.system(# send keys
              'cls'
              if os.name == 'nt'
              else 'clear')

dict(hello='hello')

def print_smooth(string):

    punctuation = [".", "!", "?"]
    
    for letter in string:
        stdout.write(letter)
        time.sleep(.035)
        stdout.flush()

        if letter in punctuation:
            time.sleep(.5)


def user_input(obj, string_display=None):
    print '\n'
    complete = False

    while not complete:
        if string_display:
            if type(string_display) == dict:
                x = 1
                for k, v in string_display.iteritems():
                    print_smooth(str(k) + ': ' + v +'\n\n')
                    x += 1
            else:
                print_smooth(string_display)

        user_in = raw_input('>>> ')
        print '\n'

        if not user_in:
            print_smooth('Sorry, I didn\'t catch that. Please enter that again.\n')
            continue

        if 'INV' in user_in.upper():
            if not obj.my_inventory:
                print_smooth('Your inventory is empty')
            else:
                print_smooth('Your inventory contains: {}.\n\n'.format(', '.join(obj.my_inventory)))
                continue
        else:
            return user_in
