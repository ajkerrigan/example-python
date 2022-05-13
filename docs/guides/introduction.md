# Introduction

Python is great! Python programs are great! In fact, you probably have some amazing python programs on your computer right now.

But... 

Sharing python programs with other people isn't so great.

 - Clone the repository......................... but what if the person doesn't have a github account.

 - Send the wheel or tar.gz file................ but what if the person doesn't have the right version of python installed.


HOWEVER, WHAT IF I TOLD YOU THERE HAS BEEN A SOLUTION ALL ALONG.........

#### *PYTHON EXECUTABLE FILES*

huh?

\<image of confused person here\>


### What is an executable file?

An executable file is a file traditionally ends in ".exe" on Windows or has execution permissions set in Mac/Linux systems [`chmod +x file.exe`]. An executable file (they have also been called applications) can be placed into a computers system source or applications directory and run from the command line.

Executable files are special because they include information about the interpreter and interpreter environment inside the file.  This means that there is no need to setup an environment to run the executable. The executable should already contain the environment information.

### What is a *python* executable file?

A *python* executable file - `.pex` - is a *new* filetype that contains information about the interpreter and virtual environment which runs a python program.

### Why do you want an executable file?

Executable files - like .zip or .tar.gz files - are *very* easy to share.  They are small, *super fast*, and work seemlessly on different computers because they contain all the information needed to run the program inside the file.

**Sounds great, how do I turn my program into this magical executable file?**

Checkout the tutorials