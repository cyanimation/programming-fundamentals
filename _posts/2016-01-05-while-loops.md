---
layout: post
title:  "While Loops"
date:   2016-01-05 19:21:15
categories: 
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/OShOW_ayPvA" frameborder="0" allowfullscreen></iframe>

&nbsp;

### Loops

In our day-to-day lives and especially with our work we repeat ourselves. If
your job is to clean a building, you have likely cleaned the same area (or areas
that are similar) multiple times. If your job is to take phone calls, you may
have had calls that felt exactly the same. Regardless of your work I am sure
that you do things that sometimes become repetitive. The same thing happens in
programming except that in programming we get to automate the process so we only
have to 'say' it once. Loops are what make this possible. Python has different
kinds of loops but the first one that we will learn about is called the `while`
loop.

<span><i class="fa fa-book"></i><a href="http://python.swaroopch.com/control_flow.html#the-while-statement"> While Loops</a></span>


### The While Loop

While loops are a mechanism to repeat something *while* some condition is true.
The [syntax](http://dictionary.reference.com/browse/syntax) for a while loop
is very similar to an if statement. They both have a **keyword** followed by an
**expression** that resolves to a **boolean** value. The first line is terminated by a
**colon** and then the body of the loop is **indented**.

{% highlight python %}
while {boolean expression is true}:
    {do the things in the indented body}
{% endhighlight %}

A loop that counts to ten looks like:

{% highlight python %}
num = 1
while num < 11:
    print num
    num += 1
{% endhighlight %}

*Note*: the `+=` operator is a shortcut for `num = num + 1`.

Anything that resolves to a boolean `True` or `False` can be contained in the
expression part of the loop. You can then put anything you wish to repeat inside
the body of the loop. Imagine a loop that asks the user for various inputs based
on their responses.

<span><em><i class="fa fa-flask"></i> Try writing a program that keeps asking 'Why?' until the user enters 'just because!'</em></span>


### Infinite Loops

So imagine that you have a loop that looks like:

{% highlight python %}
happy = True
while happy:
    print "Life is just better this way!"
{% endhighlight %}

We set a variable `happy` equal to `True` and then never change it. Do you see
the problem? We are never going to stop printing that statement. This is called
an infinite loop because it repeats itself forever. If you find your program
running in an infinite loop (I promise that you will write one eventually) you
can terminate your program by pressing *Ctrl+C*. If you have ever tried to copy
some text from the terminal you may have realized that the handy *Ctrl+C*
shortcut didn't work. This is why. It is used to terminate your rogue programs.

Even though changing that `happy` variable to `False` seems ridiculous (who
would ever want to), it is important to avoid an infinite loop. You will have to
be careful when you write loops to avoid this pitfall.
