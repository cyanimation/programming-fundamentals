---
layout: post
title:  "If Statements"
date:   2015-12-17 21:04:15
categories: 
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/qYkwh7xp-K4" frameborder="0" allowfullscreen></iframe>

&nbsp;

Programs aren't very interesting when they only do one thing. We like programs
to be multi-purposed and to accept inputs. In order to accomplish this we need
some sort of control that allows us to switch on data. 

#### The if statement

<span><i class="fa fa-book"></i><a href="http://www.swaroopch.com/notes/python/#_the_if_statement"> 9.1: The If Statement</a></span>

If statements allow us to do something conditionally. 

    if (condition):
        print 'do something if our condition is true'

The if statement uses the reserved word `if` and then has parentheses which
contain a condition. Only boolean values can go inside the parentheses. If that
value is `True`, then the command(s) that are inside the if statement will be
executed.

<span><i class="fa fa-book"></i><a href="http://www.swaroopch.com/notes/python/#indentation"> 7.14: Indentation</a></span>

The if statement has a colon after the parentheses which indicates that a
**_block_** is going to follow. The contents of the block are indented in
Python. It is important that this indentation is consistent. If you indent your
blocks by a single tab, then you must always do this. If you use four spaces
then you must similarly always use 4 spaces. When you want to end the block then
you simply go back to the indentation level you were at before the if.

    if (True):
        print "I'm inside the if"
    print "I'm outside the if"

<span><em><i class="fa fa-flask"></i> Try creating your own if statement!</em></span>

#### Else

Sometimes we want to do something when a condition is `True` and something else
when it is false. An else block allows you to switch on conditions like this:

    happy = True
    if (happy):
        print "good for you"
    else:
        print "that's too bad"

You can also switch on multiple conditions using an `elif` (else if) statement.
An `elif` is just like an `if` but comes after an initial `if`.

    mood = 'Grumpy'
    if (mood == 'Morose');
        print "We should be friends"
    elif (mood == 'Grumpy'):
        print "Don't be coming around me"
    else:
        print "I guess I don't recognize your mood"

#### Complex Examples

You can imagine more complex conditions where multiple variables come into play

    age = 11
    mood = 'Grumpy'
    family_member = True
    if (mood == 'Morose' and age > 10 or family_member);
        print "We should be friends"

The above condition uses `and` and `or` to combine multiple conditions. When you
say the whole statement out loud you can tell what should happen. In this case
`mood` must be equal to `Happy` _and_ `age` must be greater than 10. Since that
combined condition is `False` we would not enter the if block. We have a third
condition though. The `family_member` condition is also part of this and since
there is an `or` combining the previous two conditions and this one, only one
_or_ the other is necessary to enter the block. Since `family_member` is `True`
we will enter.

<span><em><i class="fa fa-flask"></i> Try collecting some data from the user
(raw_input) and doing an if statement based on their response!</em></span>


#### Tip

You might look at the `=` and `==` and wonder how they are different. The single
`=` is used as the _assignment_ operator. This operator assigns variables, on
the left of the sign, the value of whatever expression is on the right. The `==`
operator is used to express boolean conditions. The two operands in this case
must be exactly equal to be evaluated as True. `42 == "42"` may look like they
are equal but they have different types. One is an `int` and the other is a
`str`. Things can never be equal if they are of different types.
