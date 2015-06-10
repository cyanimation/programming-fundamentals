
# Introduction

Any questions . . .
Review

## outline for course
- Week 1: execution, variables, booleans, if
================================================================================
- Week 2: blocks, loops, and modules
================================================================================
- Week 3: functions, scope, and exceptions
- Week 4: lists, tuples, and dictionaries
- Week 5: classes, OOP
- Week 6: TBD

# Blocks

- begin when indentation increases
- can contain other blocks
- end when indentation decreases
- contain own scope

not all programs execute line by line some jump around and skip things

```python
happy = False
if happy:
    clap = True
else:
    stomp = True
print stomp
print clap
```

# Loops

## while loop

```python
name = ''
while name != 'reed':
    name = raw_input('what is your name? ')
```

infinite loop and ctrl-c

exercise

truthy and falsey values


## special commands

pass

break

continue


## for loop and range

range(), start, stop, step

```python
for num in range(1, 50):
    if num % 3 == 0:
        print num
```

exercise


# Modules

what is a module?

how to import modules
```python
import random
import random as rand
from random import randint
from random import *
```

common modules and their uses
- sys
- os
- math
- randint


# Homework

Review your program (multiples.py)

Fibonacci sequence

Practice Questions
