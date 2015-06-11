# Lesson 2

This directory contains all of the files related to lesson #2. My lesson plan
(2_plan.md) and the file we created together in class (2.py) are found here. I
have also created a review of what we talked about in class that should be
easier to read. You can review the homework by accessing the homework directory.


## Outline

### blocks

Blocks are portions of code that encapsulate certain functionality. Last time we
talked a little bit about if statements which are a type of block. Blocks have
certain rules that apply to them. The following is an example:

```python
variable = 42
if some_condition:
  variable += 1 
  print "it's true"
print "I'm outside of the block"
```

1. they must have a colon at the end of the statement
2. any code that is inside the block must be indented (watch out for spaces vs.
   tabs. Try to be consistent)
3. anything outside of the block must be indented at the same level as the block
   statement
4. it is good practice to define variables before you enter the block so that
   you don't run into problems later on. 

### loops

There are different types of loops that you can create but they are all
virtually the same. They do have their own conveniences though.

#### while loops

While loops are a mechanism to continue to do something *while* some condition
is true.

```python
num = 0
while num < 11:
  print num
  num += 1
```

In the previous example we have a while loop that counts to 10. It will continue
to print `num` and increment `num` until it is greater than or equal to 11 at
which time it ends. You may notice that it is formatted very similar to our if
statement. That is because it is also a block. It is important that the same
rules that applied with a colon and indentation are followed here.

#### for loops

For loops are very similar to while loops but they provide us with a different
way of thinking about looping. We get to define a fixed end in the actual
looping statement.

```python
for num in range(1,11,1):
  print num
```

This code is two lines shorter than the while loop. This is because for loops
are very good at doing things a certain number of times. This is also a block
and must have the colon and indentation.

There is a special function we are using to get the range of numbers we want. It
is the `range()` function. The range function allows us to loop a specific
number of times. It takes 3 arguments `range(start, stop, step)`. The start is
the number you want to begin at. The stop is the number you want to stop before
(11 will make it so 10 is the last number we print). Step is the number we want
to increment by through each loop or iteration. If we were to pick a step of 2
we would get the output: `1, 3, 5, 7, 9`.


### special commands

Loops have some special commands that make it easier to work with the looping
flow. These are `break`, `continue` and `pass`.

```python
num = 0
while True:
  if num == 5:
    num += 1
    continue
  print num
  num += 1
  if num == 11:
    break

if i_dont_know_what_to_do:
  pass
```

The continue statement simply skips the rest of the loop and starts on the next
iteration. The break statement will completely break out of the loop and
continue execution where the block ends. `pass` is what we call a noop (pronounced
NO-op and stands for no operation). This does nothing. If we didn't put `pass`
in the `if` statement above though the program would not be able to run. The
`pass` simply allows us to move on in our program.

### modules

Modules are very useful to use in our programs. They are pieces of code that
someone else wrote (they could even be your own modules) that you can import
into your program. They have functions on them that you can call to perform some
kind of functionality.

Some common modules are `sys`, `os`, `math` and `random`. These are really handy
and one of my favorites is `random`. We could create a little dice rolling
program using `random`:

```python
import random
print random.randint(1,6)
```

This very simple program will print out a random number between 1 and 6. 

You can import modules in various ways:
- `import random` will simply import all of random's functions prefixed by
    random as we saw in the example above.
- `import random as rand` will allow you to shorten the command like: `print
    rand.randint(1,6)`
- `from random import randint` will allow you to call `randint` without any
    prefix: `print randint(1,6)`
- `from random import *` will import all of randoms methods in a manner that you
    don't have to prefix them (I don't recommend doing this)
