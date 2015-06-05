# Lesson 1

This directory contains all of the files related to lesson #1. My lesson plan
(1_plan.md) and the file we created together in class (1.py) are found here. I
have also created a review of what we talked about in class that should be
easier to read. You can review the homework by accessing the homework directory.


## Outline

### executing a program

We learned that you can create a program by simply writing a python command:
  ``` python
  print 'hello world' 
  ```
and then saving the file you have created (e.g. hello_world.py) and then running
the file in a terminal (ensuring that the directory of your terminal is the same
as where your file is. A brief lesson on using the terminal can be found
[here](http://gr8idea.info/os/tutorials/linux/cd.html)):
  ```
  python hello_world.py
  ```

This will print out 'hello world' (without quotes) in your terminal

We also learned that you can create comments by putting a '#' at the beginning
of a line. We can also create a multi-line comment by putting triple quotes
around your text:
  ```python
  # a single line comment
  '''
  this is a multi-
  line comment
  '''
  ```


### data types and variables

A data type is simply the type of data we can store in programs. Python has a
fairly simple set of data types. 

- integer (int) which are numbers like 1, 4, 7
- floating point (float) which are numbers like 3.5, 6.2, 8.9
- string (str) which is simply a collection of characters (any character you
    wish like: 'askj#@lk14p') surrounded by quotes (' or ")

You can manipulate data using operators (+, -, *, /). The obvious math
operations like `1+2` work but we also have other operations like `'I like ' +
'britney'`. This operation will concatenate (or combine) the two strings into a
single string.

variables are simply a way to keep track of the values you want to manipulate.
They act as boxes to hold data types. You can create a variable by doing the
following:
  ```
  my_name = 'reed'
  my_age = 26
  ```
The first variable will hold a string with the value of 'reed' and the second
will hold an integer with the value of 26

Variable names have specific rules. They have to be single word (no spaces) and
can have numbers, letters or underscores. They also cannot begin with a number
and are not case sensitive (meaning SPAM does not equal spam).



### special functions

There are certain functions that Python gives us to make life easy for us. We
know that the `print` function allows us to print messages to the console
(terminal). We also learned about:

- `raw_input('message')` which allows you to print a message and collect the
    user's input
- `str()` which turns your variables into strings
- `int()` which [parses](http://en.wikipedia.org/wiki/Parsing) (or transforms) a
    string into an integer
- `float()` which parses a string to a floating point
- `len()` which returns the length of a string (how many characters it has) as
    an integer



### boolean values and expressions

Another really important data type is called a boolean (bool) named after the
great mathematician [George Boole](http://en.wikipedia.org/wiki/George_Boole).
These values can be True or False. That's it! Even though these are very simple,
they are very important. 

We can create variables that hold bools:
  ```python
  happy = True
  ```
True and False are special words in Python and must be capitalized.

Booleans also can be operated on with certain operators (<, >, <=, >=, ==, !=,
not, or, and). 
  ```python
  3 < 4
  '4' != 4
  42 == 42
  1 < 2 and 2 < 3
  ```


### control flow (if, elif, else)

We want to be able to use boolean expressions to create interesting programs. We
can create different paths of execution through our program by creating if
statements:
  ```python
  happy = False
  tired = True
  if (happy):
    print "I'm so happy today!"
  elif (tired):
    print "I can't be happy if I am tired"
  else:
    print "I am not aware of my feelings"
  ```
