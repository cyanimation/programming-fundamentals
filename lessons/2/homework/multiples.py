#!/usr/bin/env python

# import some modules so that we get some extra functionality
import os
import sys

# clear the console screen
os.system('clear')

# ask for your n
n = int(raw_input('What is the number you want to loop till? '))

# keep track of the sum
total = 0

# loop until n
for i in range(n):
    # if i is divisible by 3 or 5 then add to sum
    if i % 3 == 0 or i % 5 == 0:
        total += i

# print the answer
print total

# wait for the user to press enter to quit
raw_input('\nPress enter to quit...')

# clear the console screen
os.system('clear')
