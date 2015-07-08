#!/usr/bin/env python

# import some modules so that we get some extra functionality
import os
import sys
import random
import time

def do_question(wait_responses, responses):
  # A. Allow the user to enter their question
  question = raw_input("What is your question? ")
  # B. Display an in progress message( i.e. "divining...")
  print wait_responses[random.randint(0, len(wait_responses)-1)]
  time.sleep(2)
  # C. Create many responses, and show a random response
  print responses[random.randint(0, len(responses)-1)]

def main():
  ''' This is the main function that is our initial entry point into our program '''
  # clear the console screen
  os.system('clear')

  fortunes_filename = 'fortunes.txt'
  responses_filename = 'mystic_responses.txt'
  wait_responses_filename = 'wait_responses.txt'

  # keep track of the fortunes and responses
  responses = []
  fortunes = []
  wait_responses = []

  # read all of the lines from the fortunes file into a list
  with open(fortunes_filename) as f:
    fortunes = f.readlines()

  # read all of the lines from the responses file into a list
  with open(responses_filename) as f:
    responses = f.readlines()

  # read all of the lines from the responses file into a list
  with open(wait_responses_filename) as f:
    wait_responses = f.readlines()

  ## Start Here

  option = 0
  while option > -1:

      # 1. Ask the user to ask a question or receive a fortune
      try:
          option = int(raw_input("Question(0), Fortune(1), Quit(-1) : "))
      except Exception as e:
          print "I didn't recognize your input"
          sys.exit()

      # For Questions:
      if option == 0:
          do_question(wait_responses, responses)

      # For Fortunes:
      elif option == 1:
          # A. Display an in progress message( i.e. "divining...")
          print wait_responses[random.randint(0, len(wait_responses)-1)]
          time.sleep(2)
          # C. Create many responses, and show a random response
          print fortunes[random.randint(0, len(fortunes)-1)]

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




















