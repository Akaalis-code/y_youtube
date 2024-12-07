## Problem statement 
    Matplotlib function  "matplotlib.pyplot.show()" which was supposed to plot the graph in an interactive GUI interface
    is not popping that interactive window.
    But the plots can be saved in image format to local storage 

    Warning it shows as below when show() method is called
    >>> UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown

## Reason for problem
    In ubuntu version that I am using 24.04 SYSTEM PYTHON doesnt allow to install any libraries into it anymore
    May be to leave SYSTEM PYTHON undisturbed as OS might be dependent on it
    Instead we have to create virtual environements of python and install any libraries in them .
    And this matplotlib requires a GUI tool which it can use to show that interactive window.

## Solution 
    Any of the GUI tools for linux like "tkinter" or "qt" can be installed and it works fine.
    Here I am going to install tkinter
        > apt list --installed | grep -i python3-tk   ## check if this "python3-tk" is already installed 
        > sudo apt install python3-tk                 ## If not there use APT to install it 


Python 3.7.6
Type "help", "copyright", "credits" or "license" for more information.
>>> import tkinter      ## To check if its properly installed or not 



## Some tools of matplotlib

    >>> import matplotlib
    >>> print(matplotlib.get_backend())  ## To get info of what backend is matplotlib using for interactive window
                                            As of now its using 'tkagg'


