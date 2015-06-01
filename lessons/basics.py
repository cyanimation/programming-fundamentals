#!/usr/bin/env python

# import some modules so that we get some extra functionality (don't worry about this yet)
import os
import sys

# clear the console screen
os.system('clear')

# print the message
# the comma at the end ensures that we don't get a newline after the message
print 'Hello, what is your name? ', 

# collect the user input into a variable
name = raw_input()

# print the response using string concatenation
# the \n is the special character for a newline
print '\nIt is a pleasure to meet you ' + name + '!\n'

# tell the user how long the name is
print 'Your name is ' + str(len(name)) + ' characters long\n'

print 'How old are you? ',

# convert the input to a number (this could fail if the input isn't a number)
age = int(raw_input())

print '\nAnd have you already had a birthday this year (y/n)? ',

# get the answer concerning the past birthday and save it as a boolean
past_birthday = raw_input()

# change the 'y' or 'n' to a True or False
if past_birthday == 'y':
    # go ahead and use the same variable if you want. Just don't get mixed up
    past_birthday = True 
elif past_birthday == 'n':
    past_birthday = False
else:
    # make sure that you use the right quotes (' vs ")
    print "\nI didn't understand your response."
    raw_input('\nPress enter to quit...')
    # clear the console screen
    os.system('clear')
    # exit the program
    sys.exit()

# calculate the year
# an 'if' statement can be on a single line like this
# The parentheses are to enforce a specific order of operations. Without them
# this expression will not evaluate correctly.
year = 2015 - age - (0 if past_birthday else 1)

# conver the number back to a string because you can't add a number and a string
print '\nI know what year you were born in. It was ' + str(year) + '.'

# wait for the user to press enter to quit
raw_input('\nPress enter to quit...')

# clear the console screen
os.system('clear')
