---
layout: post
title:  "Functions"
date:   2016-06-10 01:00:00
categories: 
---

<span><i class="fa fa-book"></i><a href="http://python.swaroopch.com/control_flow.html#the-for-loop"> For Loops</a></span>

<span><em><i class="fa fa-flask"></i>Try running the for loops above with both of the range functions I have shown! One should work and the other should fail!</em></span>

Functions
- What is a function?
- How can I make one?
- Why should I make one?

More Functions
- Return values and statements
- None
- Calling a function with keyword arguments
- Scope

Error Handling
- Exceptions
- With Resources

# Functions

You have been using functions in your programs already. `int()`, `str()` and
`raw_input()` were all functions that we were able to call. These functions are
special functions specific to Python but there really isn't anything special
about them other than that they come with the language. We will learn how to
create our own functions.

Functions (also known as methods or routines), like many things in programming
come from math. If you can remember your Algebra class where you learned about
the famous function `f()` as in `f(x) = 2x + 3` you will likely be able to
understand programming functions as well. In Algebra you may remember that
functions will create some kind of line or curve. The function that I referenced
above will create a curved line (parabola). This is because as we substitute
various values for x, the function will output different results. Lets look at a
table of some possible input values:

| x    | f(x)   |
| ---- | ------ |
| -3   | -3     |
| -1   | 1      |
| 0    | 3      |
| 1    | 5      |
| 3    | 9      |

Notice that the function `f()` doesn't really care what anyone else calls the
value going in to the function. It simply renames it to x once it gets the
value. For example, lets say we had a variable called `secret_number` and we set
the value to 5 and then pass `secret_number` to `f()`. The function `f()` doesn't care
that we called that number secret_number because it immediately renamed the
value to x at the beginning of the function. This is because of something we
call scope (see the section later in this outline on scope).

## How can I make functions?

You can make your own functions by following a few rules:

1. begin your function declaration with the def keyword
2. give your function a name (names must conform to the same standards as variables)
3. place parentheses next to the function name
4. call for any arguments (or parameters) you might need in your function (like we see in our f(x) function) which may be none. You indicate this by having empty parentheses: def function_name():
5. add a colon at the end of your signature (this indicates that we have a block)
6. indent the body of your function
7. return any values that the caller might need using a return statement
8. separate both the arguments you call for and the values you return with commas
 
{% highlight python %}
def function_name(argument1, argument2):
    print 'do something in the function body'
    return 'any values you need'
{% endhighlight %}
    
Its important to remember though that this is just a function declaration. We
haven't actually called the function yet. You have already been calling
functions so you are familiar with how this works. If I were to call the
function above I would simply invoke it by saying its name and passing in what
it is asking for: function_name('arg1', 'arg2').

## Why should I make functions?

Functions are one of the central aspects to programming languages. They help us
to separate code into its separate pieces instead of cobbling together massive
scripts that are difficult to understand. A function should do one thing which
should be obvious from its name. A function called add() should simply add
things. It should not also subtract things and then launch missiles. This is a
poor way to design programs.

Functions also make it possible to avoid code duplication. If you ever find
yourself copying code from one place to another, you should stop immediately and
write a function that you could call from both places that need the shared code.
This will make your code clearer and cleaner.

## Return values and statements

I mentioned in the rules to make functions that you can return values. We have
seen functions like `len()` that tell us how long a string is. `len()` is
returning a value to us that we can store in a variable. Any time a function
needs to let its caller know the results of its computation, it should return
those results: `return first_number + second_number`

### None

Every function returns a value even if it does not explicitly have a return
statement. Python will insert a return statement for any function that doesn't
have one: `return None`. None is a special data type. Instead of having multiple
values like other data types like integers or booleans, `NoneType` can only be
one value: None. Any function that returns None is called a void function
because it is void of any substantial return value. The value of None is like a
black hole because it is simply the absence of value.

## Keyword arguments

When we have called functions in the past we simply passed in the values the
function needed. `range(1, 10)` will allow us to loop or iterate over the values
from 1 to 9. We could be more explicit about which argument is which by
specifying its name: `range(start=1, stop=10)`. You can see that by doing this
we could then pass the arguments in a different order or even omit arguments
that don't need to be there. For example, in the `range()` function we might
want to specify a step value but not a start value because we are fine to use
the default start value of 0. We could do this by using the keyword arguments.

{% highlight python %}
for i in range(step=2, stop=10):
    print i
{% endhighlight %}
    
If we were to only pass in 2 and 10 like range(2, 10) we would be telling the
range function that we wanted to start at 2 and stop at 10. This is NOT what we
wanted. To get around that we can use the keywords. This, of course, only works
if you know the name of the arguments that the function declares.

# Scope

Scope is a word we use to indicate where a named object is defined. So far, all
of our variables have been in what we call global scope. This means that every
variable we defined was available everywhere in our program (after we declared
it, of course). When we create functions we create a new scope. This is called a
local scope. From within a local scope we can see all of the named objects from
global scope but not the other way around. Global scope cannot see local scope
objects. You can even create a local scope within a local scope. The child scope
can see what is in the parent scope but the parent cannot see what is in the
child. A great article that explains scope can be found here.

## Overriding global scope

When we create a function we get a new local scope. This local scope may create
names that already exist in a parent scope or on the global scope. This is okay
because the program will simply find our local scope version of that variable
instead of the global version. Think of this as a stack of papers. We will look
through the stack of papers from top to bottom and as soon as we find the name
we are looking for we will stop. This means that when we exit this function our
local scope is destroyed. All of the variables that existed in that local scope
will be gone. This is a big reason why we should return variables from
functions. They will be destroyed if we don't give them back to the callers of
the function.

# Exceptions

You have undoubtedly seen exceptions in your programs. When your program didn't
run correctly because of some error, you were experiencing an exception. Some
exceptions you may have seen are TypeError, ZeroDivisionError, SyntaxError or
IndentationError. These occur when there is unexpected behavior in the program
and the computer does not know how to recover. You can tell your program how to
handle behavior that may be unexpected though. The best way to do that is to
simply create an if statement that accounts for things like dividing by zero. If
you cannot create and if statement though you can wrap your code in a special
kind of block. This is called a try, except block.

{% highlight python %}
try:
    print 13 / 0
except ZeroDivisionError as e:
    print "You can't divide by zero dummy. The universe is now crumbling"
    print str(e)
{% endhighlight %}

Since this is a block, it looks very similar to the other blocks we have
created. We put a colon at the end of the statement and then make sure that the
body of the block is indented. We can catch the specific type of error we might
be expecting or we can simply catch all errors by only declaring except without
any Error or by declaring except Exception as e if we want to access the
Exception variable. It is important to try to catch any exceptions that may crop
up in your code so that your code will continue to run. Exceptions are the kind
of thing that can ruin your day.
