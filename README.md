A collection of IPython Notebooks for teaching Python.
---

Here is the [index page](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/intro_programming_index.ipynb), as students see the notebooks, and the [course syllabus](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/syllabus.ipynb).
Goals:
---
- Introduce students as quickly as possible to the basics of programming, and then help them choose an interesting project that they are capable of completing.
- Introduce best practice as early as possible, while remaining accessible to students with zero background in programming.

Contributing - Brief:
---
On an Ubuntu system:
### Clone this repository into a local directory
    $ git clone https://github.com/ehmatthes/intro_programming
### Install IPython Notebook
    $ sudo apt-get install ipython-notebook
### Open the notebooks locally:
    $ cd intro_programming/notebooks
    $ ipython notebook

This will open a browser, and you can click on the notebook you'd like to edit.

There may be a bit more involved in a full setup, depending on which versions of Python you have on your system, but that will get you up and running. If you have any questions about getting the project running locally, drop a note in [Issue 11](https://github.com/ehmatthes/intro_programming/issues/11), or get in touch with me directly. I can be reached by email, ehmatthes at gmail, or on twitter [@ehmatthes](https://twitter.com/ehmatthes).

Thanks for looking!

Contributing - Detailed
---
These notebooks focus on Python 3.3, but they also show some Python 2.7 code. You may run into trouble working with the notebooks if you only have one version of Python, and one version of IPython Notebook on your system. This is how I set up my Ubuntu 12.04 system.

Add a ppa that has old and new versions of Python, and use the ppa to install Python 3.3

    sudo apt-get install python-software-properties
    sudo add-apt-repository ppa:fkrull/deadsnakes    
    sudo apt-get update    
    sudo apt-get install python3.3

Install the correct versions of ipython, ipython-notebook, ipython3, and ipython3-notebook:

    sudo apt-get install ipython=0.13.2-1~ubuntu12.04.1
    sudo apt-get install ipython-notebook=0.13.2-1~ubuntu12.04.1
    sudo apt-get install ipython3=0.13.2-1~ubuntu12.04.1
    sudo apt-get install ipython3-notebook

- Now the command `ipython notebook` should start an IPython Notebook session with your system's standard version of Python.
- The command `ipython3-notebook` should start an IPython Notebook session using Python 3.3.
- I like to test which version of Python is being used with `print(3/2)`. If you Python 3.3 is being used, you will see `1.5`, and if Python 2.7 is being used you will see `1`.
- Again, if you are having trouble with any of this drop a note in [Issue 11](https://github.com/ehmatthes/intro_programming/issues/11), or feel free to get in touch directly.
