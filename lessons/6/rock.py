#!/usr/bin/env python

import sys
import random
import os
import time


def print_rock():
    print '________            ______  '
    print '___  __ \______________  /__'
    print '__  /_/ /  __ \  ___/_  //_/'
    print '_  _, _// /_/ / /__ _  ,<   '
    print '/_/ |_| \____/\___/ /_/|_|  '


def print_paper():
    print '________                            '
    print '___  __ \_____ _____________________'
    print '__  /_/ /  __ `/__  __ \  _ \_  ___/'
    print '_  ____// /_/ /__  /_/ /  __/  /    '
    print '/_/     \__,_/ _  .___/\___//_/     '
    print '               /_/                  '


def print_scissors():
    print '________     _____                                   '
    print '__  ___/________(_)__________________________________'
    print '_____ \_  ___/_  /__  ___/_  ___/  __ \_  ___/_  ___/'
    print '____/ // /__ _  / _(__  )_(__  )/ /_/ /  /   _(__  ) '
    print '/____/ \___/ /_/  /____/ /____/ \____//_/    /____/ '


def print_lizard():
    print '___________                    _________'
    print '___  /___(_)___________ _____________  /'
    print '__  / __  /___  /_  __ `/_  ___/  __  / '
    print '_  /___  / __  /_/ /_/ /_  /   / /_/ /  '
    print '/_____/_/  _____/\__,_/ /_/    \__,_/'


def print_spock():
    print '________                   ______  '
    print '__  ___/______________________  /__'
    print '_____ \___  __ \  __ \  ___/_  //_/'
    print '____/ /__  /_/ / /_/ / /__ _  ,<   '
    print '/____/ _  .___/\____/\___/ /_/|_|  '
    print '       /_/                         '


def print_options(options):
    """ prints the options to the screen """
    os.system('clear')
    print "Pick why dontcha"
    for i, option in enumerate(options, start=1):
        print "%d. %s" % (i, option)

def print_score(score):
    print "\n\nYou have won %d times" % score[0]
    print "The computer has won %d times" % score[2]
    print "There have been %d draws" % score[1]


def lookup_choice(choice, choices, indices):
    """ converts an int to the choice string """
    return indices[choice]


def get_user_choice(choices, indices):
    return lookup_choice(int(raw_input())-1, choices, indices)


def get_choice(options, indices):
    """ gets the computer's choice """
    return lookup_choice(random.randint(0, len(options)-1), options, indices)

def print_finder(option):
    if option == 'Rock':
        print_rock()
    elif option == 'Paper':
        print_paper()
    elif option == 'Scissors':
        print_scissors()
    elif option == 'Lizard':
        print_lizard()
    elif option == 'Spock':
        print_spock()
    else:
        print "I don't know your option: " + str(option)
        sys.exit()


def beats(choice, computer_choice, choices):
    """ determines if choice beats computer_choice. 1: win, 0: draw, -1: loss """
    if choice in choices[computer_choice]:
        print 'You lose!\n\n'
        print_finder(computer_choice)
        print '\n\n%s\n\n' % choices[computer_choice][choice]
        print_finder(choice)
        return -1
    if computer_choice in choices[choice]:
        print 'You win!\n\n'
        print_finder(choice)
        print '\n\n%s\n\n' % choices[choice][computer_choice]
        print_finder(computer_choice)
        return 1
    else:
        print '\n\nIt was a draw!:\n\n'
        return 0


def get_score(outcome, score):
    """ determines the new score based on the outcome """
    if outcome == 1:
        return (score[0]+1, score[1], score[2])
    elif outcome == 0:
        return (score[0], score[1]+1, score[2])
    else:
        return (score[0], score[1], score[2]+1)


def play(score, choices, indices):
    """ performs the basic rock, paper, scissors logic """
    valid = False
    tries = 0
    while not valid:
        tries += 1
        #try:
        print_options(indices)
        choice = get_user_choice(choices, indices)
        valid = True
        tries = 0
        #except Exception as e:
            #print "I'm sorry, I didn't get that. Try again.\n"
            #print str(e), type(e)
            #if tries == 10:
                #sys.exit()
    computer_choice = get_choice(choices, indices)
    os.system('clear')
    print 'The computer chose\n\n'
    print_finder(computer_choice)
    time.sleep(1.5)
    os.system('clear')
    score = get_score(beats(choice, computer_choice, choices), score)
    print_score(score)
    return score
    

def main():
    tries = 0
    keep_playing = True
    indices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    choices = {
        'Rock': {
            'Scissors': 'crushes', 
            'Lizard': 'crushes'
            }, 
        'Paper': {
            'Rock': 'covers', 
            'Spock': 'disproves'
            }, 
        'Scissors': {
            'Paper': 'cuts', 
            'Lizard': 'decapitates'
            }, 
        'Lizard': {
            'Paper': 'eats', 
            'Spock': 'poisons'
            }, 
        'Spock': {
            'Rock': 'vaporizes', 
            'Scissors': 'smashes'
            }
        }
    score = (0, 0, 0)
    while True:
        tries += 1
        #try:
        score = play(score, choices, indices)
        keep_playing = False if int(raw_input("Quit (0) or play again (1)? ")) == 0 else True
        if not keep_playing:
            os.system('clear')
            print "Thanks for playing!"
            time.sleep(1)
            os.system('clear')
            sys.exit()
        tries = 0
        #except Exception as e:
            #print "I didn't catch that. Try again."
            #print str(e), type(e)
            #if tries == 10:
                #sys.exit()
            


if __name__ == '__main__':
    main()
