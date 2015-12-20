---
layout: post
title:  "Git and GitHub"
date:   2015-12-17 21:05:15
categories: 
---

Git is a tool that allows you to save different versions of your code. Since you
will be changing your programs as they evolve it is really handy to have
something that easily manages all of your various versions. Git is a lot more
powerful than how we will use it in this class but it is one of the most
important tools in a developers toolbelt.

The next two videos are optional but highly recommended. They talk about what
version control is and what Git is. The final video is required and describes
how we will use Git and GitHub for this class.

&nbsp;

<iframe src="https://player.vimeo.com/video/41027679" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

&nbsp;

<iframe src="https://player.vimeo.com/video/41381741" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

&nbsp;

<iframe width="560" height="315" src="https://www.youtube.com/embed/EJMahhKXlKw" frameborder="0" allowfullscreen></iframe>

&nbsp;

### Summary

#### Fork the repository

In order to get the projects that I have on GitHub into your own free account
you will need to fork them. You will find a 'fork' button in the repository
(repo).  After clicking it you will be redirected to your personal GitHub
account inside your recently forked repo.

#### Clone your forked version

The repo is still only on the GitHub server. You need to create a local copy (or
clone) in your own environment. Go to the terminal and write the following
command (replacing the URL with your repo URL):

    git clone https://github.com/reedcwilson/python-execution.git

After pressing enter you will see some output in the terminal. This is Git doing
its work.

#### Enter the local repository

After Git has finished cloning the repo change your current directory in the
terminal to your new local repo.

    cd python-execution

You should now be able to run `git status` and see that you are inside of a Git
repository.

#### Make your changes

Now is where you do your work. You will modify or create files for your
programs. You can change the files however you wish and then consult Git when
you are ready to save a version.

#### Check status

You can see where you stand with Git by typing in `git status`. Git will tell
you what has changed. This is a useful command to make sure you know what will
be committed to the repository.

#### Stage and commit

When you are ready to create a new version you will first need to stage your
changes.

    git add .

The `.` here means that you want to stage everything that is already being
tracked. You can specify what you want to stage by typing the file's name
explicitly.

After you have staged your changes you are ready to commit them to the
repo. 

    git commit -m "made the program work"

We use the `-m` option to specify a commit message. If you don't include a
message then Git will open an editor for you to add one so its really just
easier if you provide one. 

#### Push your commits to the remote

When you have made your commits you are ready to push your changes back to the
remote server.

    git push origin master

`origin` is the alias by which Git knows our remote server. You don't have to
worry about this because we are just going to use the remote that we cloned it
from. This will always be origin.

`master` is the branch we are on. Git allows you to create various branches to
make any changes you make conflict less with each other. We won't be using this
either so your will always be `master` in this class.


#### Tip

In the same way that you should save your documents often to avoid losing
things, it is a good idea to make frequent commits to Git. Frequent commits make
it easy to roll back to a very specific moment. If you are ever having to say
_and_ in your commit message it probably means you could have made your commits
more granular.
