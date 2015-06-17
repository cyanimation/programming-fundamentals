
# Introduction

Any questions . . .
Review

## outline for course
- Week 1: execution, variables, booleans, if
- Week 2: blocks, loops, and modules
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
- Week 3: functions, scope, and exceptions
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
- Week 4: lists, tuples, and dictionaries
- Week 5: classes, OOP
- Week 6: TBD



# Functions

You already know these. `int()`, `raw_input()`, `str()` are all functions.

## How can I make my own?

You create a function as follows:

```python
def function_name(parameter):
  print 'you entered a function ' + str(parameter)
```

1. Functions are defined with a `def` keyword
2. The function name must conform to the same naming standards as variable names
3. A colon at the end (indicates a block, although this is a special kind of
   block)
4. An indentation for the body of the function
5. Parameters can be passed into functions and must be declared in the function
   definition
6. Functions are called just like we have already been doing it so far:
    ```python
    function_name('reed')
    ```

Try it!


## Why functions?
- to be able to reuse code
- to separate logic into pieces that do only one thing
- to give to other functions as arguments `add()`


## Return values and statements
You can give things back to the caller of the function with the return
statement:

```python
def get_my_name():
  return 'reed'

name = get_my_name()
```

you can put the result of one function inside the argument of another function
```python
print 'the length of my name is: ' + str(len('Reed Wilson'))
```


## None
This has a type but it doesn't ever have a value. Its value is *None*

A function that doesn't have a return statement will return `None`


## Keyword Arguments
You can specify the name of a functions argument and then give them out of
order:
```python
random.randint(end=10, sep=1)
```



# Scope
global scope vs local scope

```python
name = 'reed'

def my_func(age):
  height = 71
  print 'my name is: ' + name
  print 'my age is: ' + str(age)
  print 'my height is: ' + str(height)

my_func(26)
print height
```

What if I override the global scope in a local scope?

What will the value be in the global scope if I changed a value in the local
scope?



# Exceptions
You don't want your program to die if something bad happens. 

You would like to be able to handle even unexpected behavior.

```python
try:
  print 'my favorite number is: ' + 13
except TypeError as e:
  print 'we encountered an error: ' + str(e)
```

`Exception` catches all errors but it is good to try to catch specific errors if
you can.


# Homework

Review your program (functions.py)

Calculator

Practice Questions
