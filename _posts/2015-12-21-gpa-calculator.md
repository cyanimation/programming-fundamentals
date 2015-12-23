---
layout: post
title:  "GPA Calculator"
date:   2015-12-21 21:01:15
categories: 
---

This is an optional assignment to give you more experience with the topics of
lesson one. Like the tip-calculator this assignment provides real-world
application.

### Setup

Fork and clone the lesson one homework repository (if you didn't already for the
tip calculator assignment).

**_[Lesson 1 Homework](https://github.com/pg-programming/lesson1)_**

Open the `gpa-calculator.py` file in your text editor.

### Requirements

Write a program that does the following:

- create a variable for each class you want to include (biology, geometry, etc)
- create variables storing the credits for each grade

        a = 4
        a_minus = 3.7
        ...

- ask the user what letter grade they received for each class you chose to
    include
- calculate the points for each grade by multiplying the user's provided value
    with the credits associated with that letter grade
    
        if (biology == 'a-'):
          biology_points = a_minus * biology ...

- keep track of the total points and the total credits
- calculate the GPA: `total_points / total_credits`
- print your cumulative GPA


### Tips

1. You might notice that this program requires that you repeat very similar code
for each class you selected. Functions and loops make it so you don't have to
repeat yourself so much. For now, don't worry too much about the repetition.
You might not want to select too many classes right now though.
2. Use the following table (or some variation) to calculate the number of points to
award each grade:

| Range  | Letter | Points |
| :----  | :----- | :----- |
| 93-100 | A	    | 4.00   |
| 90-92	 | A-	    | 3.70   |
| 87-89	 | B+	    | 3.40   |
| 83-86	 | B	    | 3.00   |
| 80-82	 | B-	    | 2.70   |
| 77-79	 | C+	    | 2.40   |
| 73-76	 | C	    | 2.00   |
| 70-72	 | C-	    | 1.70   |
| 67-69	 | D+	    | 1.40   |
| 65-66	 | D	    | 1.00   |
| 65-0	 | F	    | 0.00   |
