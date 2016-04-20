---
layout: post
title:  "Special Commands"
date:   2016-01-05 19:23:15
categories: 
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/OShOW_ayPvA" frameborder="0" allowfullscreen></iframe>
&nbsp;

Python has some special commands, `break`, `continue`, and `pass`, that give you
more control over your loops and blocks. 

### Break

The `break` command allows you to exit a loop prematurely. 

{% highlight python %}
while True:
    favorite_food = raw_input('What is your favorite food?')
    if favorite_food == 'broccoli':
        print "We are through here!"
        break
    print "That's a good one! Let's see what your friends think"
{% endhighlight %}

You would obviously want to place the break command inside of a conditional
statement like the loop above. One thing you might notice is that we could avoid
using the break command in the example loop by simply setting a `likes_broccoli`
variable and then placing the last `print` in an else statement. 

{% highlight python %}
likes_broccoli = False
while not likes_broccoli:
    favorite_food = raw_input('What is your favorite food?')
    if favorite_food == 'broccoli':
        print "We are through here!"
        likes_broccoli = True
    else:
        print "That's a good one! Let's see what your friends think"

{% endhighlight %}

We can often avoid the `break` command with some careful structuring but it is
sometimes really handy to use which is why we are learning about it.

<span><i class="fa fa-book"></i><a href="http://python.swaroopch.com/control_flow.html#break-statement"> The Break Statement</a></span>

### Continue

The `continue` command allows you to *continue* the next iteration without
covering the rest of the block. The following example prints all of the numbers
from 1 to 20 except those that are multiples of 3. It uses the
[modulus](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic)
operator to find out which ones are multiples of 3.

{% highlight python %}
for num in range(1, 21, 1):
    if num % 3 == 0:
      continue
    print num
{% endhighlight %}

We could restructure this example just like we did with the `break` example so
that we wouldn't have to use the `continue` command by putting the if statement
around the print.

{% highlight python %}
for num in range(1, 21, 1):
    if num % 3 != 0:
        print num
{% endhighlight %}

Again, you should often be able to avoid using the command but it can come in
handy.

<span><i class="fa fa-book"></i><a href="http://python.swaroopch.com/control_flow.html#continue-statement"> The Continue Statement</a></span>

### Pass

The `pass` command is what we call a noop (pronounced NO-op and means that there
is no operation). You might be wondering why you would want something that does
nothing in your code. What the `pass` command allows you to do is stub your code
out. There are times where you know that you are going to use an if statement
but don't know what to do in the block.

{% highlight python %}
if something_cool_happens:
  pass
{% endhighlight %}

If we didn't put `pass` in the if statement above, the program would not be able
to run. The `pass` simply allows us to write a program that compiles.

<span><em><i class="fa fa-flask"></i>Try writing some loops that break out early and continue based on some of your own conditions!</em></span> 
