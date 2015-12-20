---
layout: post
title:  "Data Types"
date:   2015-12-17 21:02:15
categories: 
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/Qnmswnu0BSA" frameborder="0" allowfullscreen></iframe>

&nbsp;

### Summary

#### Data Types

A data type is simply the type of data we can store in programs. Python has a
fairly small set of data types. 

- integer (int) which are numbers like `1`, `4`, `7`
- floating point (float) which are numbers like `3.5`, `6.2`, `8.9`
- string (str) which is simply a collection of characters (any character you
    wish like: `askj#@lk14p`) surrounded by quotes (' or ")
- boolean (bool) which can be either `True` or `False` (see [George
     Boole](https://en.wikipedia.org/wiki/George_Boole)). `True` and `False` are
     special words in Python and are reserved for their raw values. That means
     that you may not use them when naming things.

#### Operators

You can manipulate data using operators (+, -, *, /, <, >, etc). The obvious math
operations like `1+2` work but we also have other operations like `'I like ' +
'britney'`. This operation will concatenate (or combine) the two strings into a
single string.

Try printing out to the terminal screen some math operations:

    # use the exponentiation operator
    print 2**3
    print 'reed likes' + ' to program'

Running this program should produce: `8` and `reed likes to program`.

In addition to the math operators and a few that work on strings there are also
a number of booleans operators (<, >, <=,
>=, ==, !=, not, or, and). 

    print 3 < 4
    print '4' != 4  # strings are never equal to numbers
    print 42 == 42
    print 1 < 2 and 2 < 3

Running this program should produce: `True` 4 times.

#### Variables

Variables are simply a way to keep track of the values you want to manipulate.
They act as boxes to hold data types. You can create a variable by doing the
following:

    my_name = 'reed'
    my_height = 70.9375
    happy = True

The first variable will hold a string with the value of `reed`, the second
will hold an floating point with the value of `70.9375`, and the third will hold a
boolean with the value of `True`.

Variable names have specific rules. They have to be a single word (no spaces)
and can have numbers, letters or underscores. They cannot begin with a number
and are case sensitive (meaning `SPAM` does not equal `spam`).
