---
layout: post
title:  "Built-in Functions"
date:   2015-12-17 21:03:15
categories: 
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/iTjxPj5E_OI" frameborder="0" allowfullscreen></iframe>

&nbsp;

You might remember functions from your Algebra days.

    f(x) = 2x + 3

We say that this is a function of `x` meaning that `x` is our variable.
Functions in math, like the one above, accept inputs and produce outputs. When
we 'run' the function above we see the following results:

    f(0) = 2(0) + 3  -->  3
    f(1) = 2(1) + 3  -->  5
    f(2) = 2(2) + 3  -->  7
    f(2) = 2(3) + 3  -->  9

Functions in programming look a little different but the same concepts apply.
The language gives us some build-in functions to make life easy. We have already
seen the `print` function which allows us to print messages to the terminal. The
print function is a little special because it doesn't have parentheses but it is
a function.

Functions are called by specifying the name: `func` and then putting parentheses
after the name: `func()`. Functions often take arguments which you will put
place inside of the parentheses: `func(arg1, arg2)`. Many (but not all)
functions return things from them.

#### **`string <-- raw_input('message')`**

Prints out the given message to the terminal and then waits for the user to type
in a message and press enter. The message the user typed is returned from the
function as a `string`.

#### **`string <-- str(anything)`**

Takes any data type and converts it to a `string`.

#### **`int <-- int(string)`**

Takes a `string` representation of a number (`"42"`) and converts it to an `int`.

#### **`float <-- float(string)`**

Takes a `string` representation of a number (`"3.14"`) and converts it to a `float`.

#### **`int <-- len(string)`**

Finds the length of a `string` (how many characters) and returns it as an
`int`.

<span><em><i class="fa fa-flask"></i> Try collecting some data from the user and
then print out a specialized message like "It's a pleasure to meet you {name}"!</em></span>
