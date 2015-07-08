#!/usr/bin/env python

# import some modules so that we get some extra functionality
import os
import sys

def main():
  ''' This is the main function that is our initial entry point into our program '''
  # clear the console screen
  os.system('clear')


  ## Start Here

  # You remember those multiplication tables from elementary school, right? The
  # ones where you choose a number on the top row and one on the side and see
  # where they meet on the chart? Good. It would be easy enough to just write it
  # out, but let's try using Python to our advantage.

  # GOAL

  # Create a program that prints out a multiplication table for the numbers 1
  # through 9. It should include the numbers 1 through 9 on the top and left
  # axes, and it should be relatively easy to find the product of two numbers.
  # Do not simply write out every line manually (ie print('7 14 21 28 35 49 56
  #   63') ).

    #1 2 3 4 5 6 7 8 9
  #1 1 2 3 4 5 6 7 8 9
  #2
  #3
  #4
  #5
  #6
  #7

  row_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  col_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  table = []
  for row_num in row_list:
      row = []
      for col_num in col_list:
          #add row_num * col_num to row
          print row_num * col_num
      # add your row to the table

  # print the table

  #   SUBGOALS

  #       As your products get larger, your columns will start to get crooked from
  #       the number of characters on each line. Clean up your table by evenly
  #       spacing columns so it is very easy to find the product of two numbers.


  # wait for the user to press enter to quit
  raw_input('\nPress enter to quit...')

  # clear the console screen
  os.system('clear')


# this makes it so that when you run your file that it will call the main
# function. It is always good practice to do this. We put all of the runtime
# functionality in the main function
if __name__ == '__main__':
  main()
