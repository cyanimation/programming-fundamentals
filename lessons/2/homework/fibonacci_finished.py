#!/usr/bin/env python

# import some modules so that we get some extra functionality
import os
import sys

# clear the console screen
os.system('clear')

# ask for the option they would prefer
option = int(raw_input('What is your preference:\n1. nth Fibonacci number\n2. last Fibonacci number <= n\n'))

# only continue if you recognize their choice
if option == 1 or option == 2:
    # ask for the n
    n = int(raw_input("\nPlease enter the number: "))
    # keep track of the current first and second numbers
    first = 0
    second = 1
    # switch on their choice for separate algorithms
    if option == 1:
        # for option 1, loop for n times
        for i in range(n):
            print first,
            temp = second
            second += first
            first = temp
        # print the answer
        print '\nThe answer is: ' + str(first)
    elif option == 2:
        # loop while we are <= to n
        while second <= n:
            print first, 
            temp = second
            second += first
            first = temp
        # print the answer
        print '\nThe answer is: ' + str(first)
else:
    print "I didn't understand your option"


# wait for the user to press enter to quit
raw_input('\nPress enter to quit...')

# clear the console screen
os.system('clear')
