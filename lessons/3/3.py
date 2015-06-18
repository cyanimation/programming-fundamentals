#!/usr/bin/env python

#==============================================================================#
#-------------------------------- Introduction --------------------------------#
#==============================================================================#

# OUTLINE:

# questions . . .

# review



#==============================================================================#
#--------------------------------- Functions ----------------------------------#
#==============================================================================#

#print 'my string' # this is weird
#raw_input(str(32))
#int(), str(), len(), float()
#print len('my string')

#def int(string):
    #pass

#def raw_input(argument):
    #return print_and_wait(str(argument))

#answer = raw_input('my message')

# how can I make my own?
#def get_reed_name():
    #print 'reed wilson'

#def get_my_name():
    #print 'britney wilson'

#get_my_name()

#1. name -- same rules as variable names
#2. def is used to begin our declaration
#3. open and close parens 
#4. arguments can be passed in as keywords
#5. functions can return values to the caller

# why should I make them?

# return values and statements

#print 'the length of my name is: ' + str(len('reed wilson'))

# none

# keyword arguments

#for num in range(step=2, stop=10):
    #print num

#def my_func(first, second):
    #print first, second

#my_func(second='wilson', first='reed')

#==============================================================================#
#----------------------------------- Scope ------------------------------------#
#==============================================================================#

#name = 'reed'

#def set_name(new_name):
    #name = new_name
    #print name


#print name
#set_name('harry')
#print name


#==============================================================================#
#--------------------------------- Exceptions ---------------------------------#
#==============================================================================#

#def fav_num(num):
    #try:
        #print 'my favorite number is: ' + num
    #except TypeError:
        #print "you didn't give me a string. make sure you do that"
        #import sys
        #sys.exit()


#fav_num(42)

try:
    print 10/0
except ZeroDivisionError:
    print 'the universe is crumbling'
    sys.exit()
except TypeError:
    pass


#==============================================================================#
#---------------------------------- Homework ----------------------------------#
#==============================================================================#

# functions.py

# calculator.py

# practice questions



#==============================================================================#
#---------------------------------- Free Time ---------------------------------#
#==============================================================================#
