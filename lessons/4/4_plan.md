
# Introduction

Any questions . . .
Review

## outline for course
- Week 1: execution, variables, booleans, if
- Week 2: blocks, loops, and modules
- Week 3: functions, scope, and exceptions
- **Week 4: lists, tuples, and dictionaries**
- Week 5: classes, OOP
- Week 6: TBD

# Intro to Lists

What is a list?

How can I create a list and access its values?

## negative indexes
```python
my_list = [1, 2, 3]
my_list[-1] == 3
```

## slices
```python
my_list = [1, 2, 3, 4, 5, 6]
list_1 = my_list[:3]
list_2 = my_list[2:4]
list_3 = my_list[3:]
```

## len(), del()
```python
len([1, 2, 3]) == 3
del(my_list[1])
```


***Activity***
Create a list containing the numbers 1-5. 
print the second number in the list


# Working with Lists

## lists with loops
```python
my_list = [1, 2, 3, 4, 5]
for num in my_list:
  print num
```

## enumerate
```python
my_list = [1, 2, 3, 4, 5]
for i, num in enumerate(my_list):
  print i, num
```


***Activity***
write program that:
Asks for the names of each space invader that has visited you in your bedroom
stores them in a list
prints the last one in the list and then deletes it
prints all the invaders

# More Operators and Member Functions

## in, not
```python
3 not in [ 1, 2, 4, 5]
```

## concatenation
```python
[1, 2, 3] + [4, 5, 6]
```

## multiplication
```python
[1, 2, 3] * 3
```

## multiple assignment
```python
name, height, age = [ 'reed', 71, 26 ]
```

## append()
```python
my_list = [1, 2, 3]
my_list.append(4)
```

## insert()
```python
my_list.insert(0, -1) # [-1, 1, 2, 3, 4]
```

## index()
```python
my_list.index(2) == 2
```

## remove()
```python
my_list.remove(3)
```

## sort()
```python
[ 4, 6, 1, 'reed', 'britney' ].sort()
[ 'Reed', 'britney', 'gary', 'Zeke' ].sort()
```


***Activity***
keep asking the user for numbers until they put -1
ask the user for a number to check to see if its in the list
sort the list
print out the list

# Strings and Tuples

mutable vs immutable

strings are lists: 
```python
'reed'[3] == 'd'
```

tuples are essentially lists that can not change (immutable) and use () instead
of []

## convert between using list() and tuple()
```python
my_list = [1, 2, 3]
print type(tuple(my_list))
```

# Reference vs Value
```python
first = 0
second = 1

# swap
temp = second
second = first
first = temp

cheese = [1, 2, 3, 4, 5]
spam = cheese
cheese[2] == 'hello'
print cheese
print spam

# WHAT?!
```

how does passing an integer to a function differ from passing a list?

copy.copy() and copy.deepcopy()

# Lists of lists -- 2D arrays/lists

# Homework

Review your program (palindrome.py)

Fix Green Eggs and Ham

Practice Questions
