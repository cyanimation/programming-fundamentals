#!/usr/bin/env python

# import some modules so that we get some extra functionality
import os
import sys

def main():
  ''' This is the main function that is our initial entry point into our program '''
  # clear the console screen
  os.system('clear')

  fortunes_filename = 'fortunes.txt'
  responses_filename = 'mystic_responses.txt'

  # keep track of the fortunes and responses
  responses = []
  fortunes = []

  # read all of the lines from the fortunes file into a list
  with open(filename) as f:
    fortunes = f.readlines()

  # read all of the lines from the respones file into a list
  with open(filename) as f:
    responses = f.readlines()

  ## Start Here

  # THE TASK:

  # 1. Ask the user to ask a question or receive a fortune

  # For Questions:
      # A. Allow the user to enter their question
      # B. Display an in progress message( i.e. "divining...")
      # C. Create many responses, and show a random response

  # For Fortunes:
      # A. Display an in progress message( i.e. "divining...")
      # C. Create many responses, and show a random response

  # 2. Allow the user to ask another question or quit


  # wait for the user to press enter to quit
  raw_input('\nPress enter to quit...')

  # clear the console screen
  os.system('clear')


# this makes it so that when you run your file that it will call the main
# function. It is always good practice to do this. We put all of the runtime
# functionality in the main function
if __name__ == '__main__':
  main()
