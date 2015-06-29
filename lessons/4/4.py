#!/usr/bin/env python

#==============================================================================#
#-------------------------------- Introduction --------------------------------#
#==============================================================================#

# OUTLINE:

# questions . . .

# review



#==============================================================================#
#-------------------------------- Lists Intro ---------------------------------#
#==============================================================================#

# What is a list?
#f(x) = 3x + 4
#my_list = [ 1, 2, 3, 4, 5, 6 ]

# How can I create a list and access its values?
#print my_list[3]

# accessing values: negative indexes, slices
#print my_list[len(my_list)-1]
#print my_list[-1]

#first_list = my_list[:3]
#second_list = my_list[1:5]
#third_list = my_list[3:]

#print first_list
#print second_list
#print third_list

# functions with lists: len(), del()
#del my_list[2]
#print my_list

#int = 3
#int('3')
#print int
## ERROR
#list = [1, 2, 3, 4]
#list('my list')
## ERROR

# Activity


#==============================================================================#
#---------------------------- Working With Lists  -----------------------------#
#==============================================================================#

# lists with loops

# enumerate

# Activity


#==============================================================================#
#---------------------- Operators and Member Functions  -----------------------#
#==============================================================================#

my_list = [ 'Reed', 'britney', 'gary', 'Zeke', 4 ]
#print 'reed' in my_list
#print 'jacob' not in my_list
#<=, not, ==, !=
## in, not

## concatenation, and multiplication
'my name is' + ' bob' == False
'bob' * 3
#new_list = my_list + [ 'sarah', 'evelyn' ]
#new_list = my_list * 2
#print new_list

## multiple assignment
#first_person = my_list[0]
#second_person = my_list[1]
#third_person = my_list[2]
#fourth_person =  my_list[3]

#first, second, third, fourth = my_list
#print third

## append(), insert(), index(), remove(), sort()
#num = 3
#num.append(4)
#my_list.append('jacob')
#my_list.remove('britney')
#my_list.sort()
#print my_list.index('Reed')
#my_list.insert(0, 'Ben')
#print my_list

#import sys
#sys.exit()

# Activity

#name = ''
#space_invaders = []
#while name != '-1':
    #name = raw_input('give me the name of all the space invaders under your bed (type -1 to quit)')
    #if name == '-1':
        #break
    #space_invaders.append(name)

#print space_invaders
#print space_invaders[-1]
#space_invaders.remove(space_invaders[-1])
#print space_invaders


#==============================================================================#
#----------------------------- Strings and Tuples -----------------------------#
#==============================================================================#

# strings

#my_list[2] = 'superman'
#print my_list
# mutable vs immutable
#my_str = [ 'm', 'y', 's', 't', 'r' ]
#my_str = 'mystr'
#my_str[2] = 'superman'
#my_str = 'mystr'
#for char in my_str:
    #print char

# c++
#string my_str = 'mystr';
#my_str[2] = '3';

# tuples
#num = 3
#my_list = [1, 2, 3, 4]
#my_tuple = (1, 2, 3, 4)

#print 'reed' == 'Reed'
#print (1, 2, 3, 4) == (1, 2, 3, 4)
#print [1, 2, 3, 4] == [1, 2, 3, 4]


#def modify_first(first):
    #first[0] = 'bob'
    #launch_missile()

#def multiply_by_10(first):
    #first = first * 10

#import copy

#num = 10
#multiply_by_10(num)
#print num
#modify_first(copy.copy(my_list))
#print my_list


# convert between using list() and tuple()
#my_tuple = (1, 2, 3, 4)
#my_list = list(my_tuple)


#==============================================================================#
#----------------------------- Reference vs Value -----------------------------#
#==============================================================================#

# how does passing an integer to a function differ from passing a list?

# copy.copy() and copy.deepcopy()


#==============================================================================#
#------------------------------- Lists of Lists -------------------------------#
#==============================================================================#

# so lists can hold bools, ints, floats, strings right? what about lists?
def print_2d(l):
    for i in l:
        for j in i:
            print j,
        print

my_list = [ ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-'] ]

print_2d(my_list)

my_list[1][1] = 'x'

print_2d(my_list)


#==============================================================================#
#---------------------------------- Homework ----------------------------------#
#==============================================================================#

# palindrome.py

# suess_fixer.py

# practice questions



#==============================================================================#
#---------------------------------- Free Time ---------------------------------#
#==============================================================================#
