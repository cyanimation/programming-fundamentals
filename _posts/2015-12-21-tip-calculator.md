---
layout: post
title:  "Tip Calculator"
date:   2015-12-21 21:02:15
categories: 
---

You have already written your first program but now you will write one that has
a real-world application. The requirements for accomplishing this assignment
will be given. 


### Setup

Fork the lesson one homework repository.

**_[Lesson 1 Homework](https://github.com/pg-programming/lesson1)_**

Clone your remote repository (replacing `reedcwilson` with your username).

{% highlight bash %}
git clone https://github.com/reedcwilson/lesson1.git
{% endhighlight %}

Change directories in your terminal to your newly cloned repository.

{% highlight bash %}
cd lesson1
{% endhighlight %}

Open the `tip-calculator.py` file in your text editor by double clicking on it
in the left pane.


### Requirements

Write a program that receives the following inputs from the user:

- the server's name
- how much the meal cost
- the tax rate as a floating point (e.g. 6.5)
- the tip percent as an integer (e.g. 15 or 20)

Print out the following results:

- The amount to tip
- The total amount for the meal
- A thank you for the server


### Tips

- Remember that percentages are often represented as numbers like 6.5% but the
    real value is 0.065.
- The user's input will always be a string. You will need to convert the
    appropriate inputs into numbers.
