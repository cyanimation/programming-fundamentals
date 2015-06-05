
# Introduction

- who am I?
- who are you and what do you do in your free time?
- who has had experience with programming?
- who knows what a programming language is?
- explain why I am using Python (and what it is)
    ```JavaScript
    function thisFunc(param) {
      if (this) {
        that();
      }
    }
    ```
    ``` Python
    def this_func(param):
      if this:
        that()
    ```
- where can I find resources?

## outline for course
- Week 1: execution, variables, booleans, if
- Week 2: blocks, loops, and modules
- Week 3: functions, scope, and exceptions
- Week 4: lists, tuples, and dictionaries
- Week 5: TBD
- Week 6: TBD


## Koding accounts

- does everyone have them set up?
- workspaces - what are they and how will we use them?
- what is a text editor?
- what is a terminal?
- how do I call programs from a terminal and what does that mean?
- IDLE (just FYI because the book uses IDLE)



# Basics

## getting started

### running basic expressions
How to run a program (Hello World)


### its okay to make mistakes.
An error just means that the program didn't work. Keep experimenting to get it
right.

its important to be precise though because computers will try to do whatever it
is you tell them to do


### order of operations

programs are full of operators and operands. Knowing the proper order that
things are executed is critical to successful programming.


## variables

### data types

- floating points
- integers
- strings

### operators with data types

```
'Alice' + ' is hungry'
'Alice' + 4
'Alice' * 5
```

### storing data types

```
name = 'Alice'
age = 7
age = age + 1
age += 1
name = 'Bob'
```

### variable names

RULES:
- single word (single_word)
- letters, numbers and underscore (_also_valid_2)
- cannot begin with number
- case sensitive (spam does not equal SPAM)
- use variable names that describe the container
- the book uses camelCase but we will use Python PEP8 standard
    (underscore_separated)


## comments
- Good programming not only ensures that the computer can understand what you
    want but also so other programmers (including yourself) can understand.
    Comments are an important part of communicating to other humans down the
    road who will read your code

## print
- print is one of the most important things you will ever learn in programming.
    You can place print statements anywhere in your code so that you can display
    a message to the screen. This can help you find the errors in your code as
    well as provide the foundation to many fun and interesting programs.

## input
- the raw_input function is how you can collect information from users who may
    run your program.

## len
- this function will tell you how many characters are in a string

## str(), int(), float()
- anything can typically be converted to a string but numbers need to be PARSED.
    Not all strings are numbers ('four' and '4'. Which one parses?)


# if, else, elif

### booleans
True and False are reserved words

#### comparison operators
- ==
- !=
- >
- <
- <=
- >=
- and
- or
- not

expressions

```
 42   <  50 == True
 50  ==  50 == True
 51  !=  50 == True
'42' !=  42 == True
```

combining expressions

```
(1 < 2) and (2 > 3) == False
(1 < 2) or  (2 > 3) == True
```

control flow

```
if name == 'Reed':
  print 'Hello Reed'
elif name == 'Britney':
  print 'Hello Britney'
else:
  print "I don't know you"
```


# Review
- variables and data types
- special functions
- booleans
- if, elif, else

# Homework

Review your program (basics.py)

## tip calculator

## grade calculator

## Practice Questions
