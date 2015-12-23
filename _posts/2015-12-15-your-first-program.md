---
layout: post
title:  "Creating and Running Python Programs"
date:   2015-12-17 21:01:15
categories: 
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/GVYBeS_UfyI" frameborder="0" allowfullscreen></iframe>

&nbsp;

### Koding

You should have a free Koding account setup.

### Text editor vs terminal 

When you first create your account you should have two separate windows on the
right-hand side. One is a text editor and the other is a terminal. The text
editor has a tab that says: Untitled.txt and has line numbers. The terminal
should have some prompt text where you can type commands.  We will use both for
programming.


### Create a program

<span><i class="fa fa-book"></i><a href="http://www.swaroopch.com/notes/python/#_using_a_source_file"> 6.6: Using A Source File</a></span>

We create programs using the text editor. Python programs consist of files that
end in a ".py" extension. An example file look like: `my-first-program.py`. It
is easiest if you don't put any spaces in your file names. The contents of the
file are what make the program work. In your first program you should try
something easy. Try using the `print` command to display something in the
terminal.

Type the following command in your text editor and then save it as
`my-first-program.py`.

    print 'hello world' 

### Execute the program

Now try executing the program that you have just created by clicking on the
terminal and typing:

    python my-first-program.py

Press 'Enter' when you are finished to execute the command. The result of this
command should print 'hello world' (without quotes) in your terminal.

Using a terminal can sometimes be challenging. A terminal is a tool that allows
you to execute commands. Almost all of the commands that we do have something to
do with the file system. Your terminal in Koding starts in your home directory.
When you saved that file you saved it to the home directory so typing `python
my-first-program.py` it was able to call the `python` command with your file
because your file was in the current directory. If it had been in a different
directory you would have had to point to that location otherwise the command
would fail. To become a little more comfortable using the terminal try going
through [this brief tutorial](http://gr8idea.info/os/tutorials/linux/cd.html).

<span><em><i class="fa fa-flask"></i> Make your own 'hello world' program!</em></span>


### Tip

<span><i class="fa fa-book"></i><a href="http://www.swaroopch.com/notes/python/#_comments"> 7.1: Comments</a></span>

You can create comments by putting a '#' at the beginning of a line. Comments
are not executed by the interpreter so they serve as notes to other developers
(or even yourself when you forget) regarding your code. You can also create
multi-line comments by putting triple quotes around your text:

    # a single line comment

    print "this will be executed because it it not commented out"

    '''
    this is a multi-
    line comment
    '''

    """
    this is also a
    multi-line comment
    """
