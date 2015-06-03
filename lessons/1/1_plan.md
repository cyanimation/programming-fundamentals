
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
- Ask for the server's name (collect in variable)
- Ask for how much the meal was (integer)
- Ask for how much the tax is (floating point)
- Ask for what the percentage of the tip is (integer) (NOTE: you will have to
    convert this to a floating point by dividing by 100)
- Print out the name of the server and the total

## grade calculator
- choose n number of classes (n being the number you choose)
- create variables storing each of the grades and their values (a: 4, a-: 3.7 etc.)
- calculate the points (grade * credits)
- calculate the gpa (sum(points) / sum(credits))
- print your cumulative GPA


## Practice Questions

1. Which of the following are operators, and which are values?
  ```
  *
  *'hello'
  -88.8
  -
  -/
  +
  +5
  ```

2. Which of the following is a variable, and which is a string?
  ```
  spam
  'spam'
  ```
3. Name three data types.

4. What is an expression made up of? What do all expressions do?

5. This chapter introduced assignment statements, like spam = 10. What is the
   difference between an expression and a statement?

6. What does the variable bacon contain after the following code runs?
  ```
  bacon = 20
  bacon + 1
  ```

7. What should the following two expressions evaluate to?
  ```
  'spam' + 'spamspam'
  'spam' * 3
  ```

8. Why is eggs a valid variable name while 100 is invalid?

9. What three functions can be used to get the integer, floating-point number,
   or string version of a value?

10. Why does this expression cause an error? How can you fix it?
  ```
  'I have eaten ' + 99 + ' burritos.'
  ```

Extra credit: Search online for the Python documentation for the len() function.
It will be on a web page titled “Built-in Functions.Skim the list of other
functions Python has, look up what the round() function does, and experiment
with it in the interactive shell.
