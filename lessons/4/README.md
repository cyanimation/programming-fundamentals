# Lesson 4

This directory contains all of the files related to lesson #4. My lesson plan
(4_plan.md) and the file we created together in class (4.py) are found here. I
have also created a review of what we talked about in class that should be
easier to read. You can review the homework by accessing the homework directory.


## Outline

### Intro to Lists

Everyone knows what a list is right? We have TODO lists, word lists, homework
lists. They are everywhere. Well, they are in computers too. Lists help us
organize values we might be interested in into a single collection. We can then
perform operations on each element of the list and add or delete items. In
Python we can create a list by doing the following:

```python
my_list = [1, 2, 3]
```

We store lists in variables like we have been doing with integers and strings.
We encapsulate or surround the values with square brackets. To get the values
out of a list we have created we do the following:

```python
my_list[1]
```

This will give us the value of `2`. What!? Shouldn't it be `1`? Nope. The answer
is `2` because in computers we almost always start at an index of `0`. The word
I used here is *index* which refers to the action of finding an object. If you
went to a library and wished to get a book, you would look up the book's index
which would lead you to where it is on a shelf. The same concept applies to
indexes (or indices) in a list. The index is the item's position in the list. We
use those square brackets after the variable name to tell Python that we wish to
index the list at the desired position.

Python allows us to do some cool things with lists. One of these is the ability
to index a list from the back instead of the front. This is called a negative
index and when performed on our list would give us the value of `3`.

```python
my_list[-1] 
```

We can also create sublists from existing lists. This is called slicing. It
looks just like indexing but we supply two values instead of one.

```python
my_list = [1, 2, 3, 4, 5, 6]
list_1 = my_list[:3]   # [1, 2, 3]
list_2 = my_list[1:5]  # [2, 3, 4, 5]
list_3 = my_list[3:]   # [4, 5, 6]
```

We are familiar with the `len()` function with strings but it can also be used
with lists to determine how many objects are in lists. 

```python
len([1, 2, 3]) == 3
```

### Working with Lists

We don't typically just create lists with all of the values in them. Usually we
get the lists dynamically (meaning we get them when the program is running
either from a user, a file, the Internet or somewhere else). This means that we
don't always know very much about our lists such as how big they are or what the
values are inside the list. For this reason we might want to loop over all of
the items in the list. You can do this like so:

```python
my_list = [1, 2, 3, 4, 5]
for num in my_list:
  print num
```

This looks almost like an English command. It is hardly cryptic and can almost
not qualify as code right? The value `num` in the loop declaration will be the
value of the current item in the list. It will update to be the next item after
each loop (or iteration).

Sometimes we want to know the index of the item in the list that we are looping
over. You can do that with the enumerate function:

```python
for i, num in enumerate(my_list):
  print i, num
```

This time we have two variables: `i` and `num`. The `i` variable will be the
index and the `num` variable will be the item in the list.


### More Operators and Member Functions

There are some keywords that we have seen already but they have different
meanings when applied to lists. The `in` keyword was used previously in a `for`
loop. When used with lists we can have Python tell us if a specific value is in
a list.

```python
3 not in [ 1, 2, 4, 5] == True
```

We can also use some of our familiar operators with lists. We can concatenate
(combine) two lists together with the `+` operator.

```python
[1, 2, 3] + [4, 5, 6]   # [1, 2, 3, 4, 5, 6]
```

We can also combine things together multiple times using the `*` operator.

```python
[1, 2, 3] * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

There might be a time when you want to set multiple values from a list at the
same time. Python allows you to do this with multiple assignment.

```python
name, height, age = [ 'reed', 71, 26 ]
```

This is all really cool but how do you add things to a list when the program is
running? Lists have functions that you can call *on* them. This means that when
you have a list like: `my_list = [1, 2, 3]` you can call functions on `my_list`.
We call these *member functions* because they are *members* of List.

#### append()
```python
my_list = [1, 2, 3]
my_list.append(4)
```

#### insert()
```python
my_list.insert(0, -1) # [-1, 1, 2, 3, 4]
```

#### index()
```python
my_list.index(2) == 2
```

#### remove()
```python
my_list.remove(3)
```

#### sort()
```python
[ 4, 6, 1, 'reed', 'britney' ].sort()          # doesn't work
# check out ASCII values for why the following list sorts funny
[ 'Reed', 'britney', 'gary', 'Zeke' ].sort()   # [ 'Reed', 'Zeke', 'britney', 'gary']
```


### Strings and Tuples

So far we have been creating lists that we can modify. This is called
*mutability* (like teenage *mutant* ninja turtles or X-men because they are
changed or mutated). We have already been exposed to lists that cannot change
though. Really? Yes, strings are an example of a list that is *immutable*. You
can treat strings exactly like you would lists aside from being able to change
the individual characters in the string. You can loop over the characters and
get the length `len()` and even index a string to get a specific character.

```python
'reed'[3] == 'd'
```

Another example of an immutable list is called a *tuple*. Tuples are just like
lists except you can't change them once they are made. You can create a tuple by
using parentheses `()` instead of square brackets `[]`.

```python
my_tuple = (1, 2, 3)
```

Sometimes we want to convert between lists and tuples. This is easy to do with
the `list()` and `tuple()` functions supplied by Python.

```python
my_list = [1, 2, 3]
print type(tuple(my_list))
```

### Reference vs Value

Something very important to understand about lists is that they are not simply a
single value. They are a collection of values. Each value in a list has a
specific address (or index) in the computer's memory. Because of this, when we
give lists to functions we might call, the computer does not copy all of the
values in the list to a function. Rather, it just gives the function a reference
to where those values exist in memory. This can cause some headache for someone
who might not be aware of what is going on. If the function changes the value in
the list we gave it without our knowing then we might be surprised when we try
to use the list later on and find that it doesn't have the values we expected.

In the example below we can see the difference between working with values and
working with references.

```python
# WORKING WITH VALUES
first = 0
second = 1

# swap
temp = second
second = first
first = temp

# WORKING WITH REFERENCES
cheese = [1, 2, 3, 4, 5]
spam = cheese
cheese[2] == 'hello'
print cheese
print spam

# >>> [ 1, 2, 'hello', 4, 5]
# >>> [ 1, 2, 'hello', 4, 5]

# WHAT?!
```

If you were able to follow the above example, you might be wondering why spam
and cheese both were changed when all we did was change `cheese[2]` to equal
`'hello'`. The reason is because when we set `spam = cheese` we were not copying
all of the values from `cheese` into a new list called `spam`. We were simply
giving `spam` the location of the first item in `cheese`. This is just like a
library. What if we were to create a bookshelf and put a bunch of books on it
and then create an index card with the name of `Fantasy` and an address of 42.
We could then simply create a new index card called `Romance` and give it the
value of `Fantasy` which is ... 42. This means that anyone who tries to find
`Romance` will be led directly to the superior genre of `Fantasy`.

You may be wondering how we can easily make copies of lists. Well, there is a
module called `copy` that you can import: `import copy`. It has two methods
called `copy()` and `deepcopy()` that you can use to copy your lists.


### Lists of lists -- 2D arrays/lists

So far, we have put numbers and strings into lists and we could imagine that
they can also hold booleans right? But what if we wanted to have a list hold ...
another list!? Wouldn't that be cool. We call this a two-dimensional array (or
list). We could print out a Tic-Tac-Toe game using a two dimensional list:

```python
def print_2d(l):
    for i in l:
        for j in i:
            print j,
        print

my_list = [ ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-'] ]

print_2d(my_list)

my_list[1][1] = 'x'

print_2d(my_list)
```

Try it out!
