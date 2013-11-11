A collection of IPython Notebooks for teaching Python.
---

Here is the [index page](http://www.introtopython.org), as students see the notebooks, and the [course syllabus](http://www.introtopython.org/syllabus.html). These are all static versions of the notebooks which have been converted to html, which are hosted at [introtopython.org](http://www.introtopython.org).

You can also view the raw notebooks using the IPython Notebook Viewer. The  [index page](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/index.ipynb) and the [course syllabus](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/syllabus.ipynb) look pretty much the same on both places for now, but they will start to differ.

Goals:
---
- Introduce students as quickly as possible to the basics of programming, and then help them choose an interesting project that they are capable of completing.
- Introduce best practice as early as possible, while remaining accessible to students with zero background in programming.

Contributing - Brief:
---
I am updating the project to facilitate generating static html files from the raw notebooks. This work requires IPython version 1.1.0, which has a slightly different installation process. I will be updating the readme shortly to reflect this different process. If you are eager to get the newer version of IPython installed, feel free to drop a note in [Issue 11](https://github.com/ehmatthes/intro_programming/issues/11), or get in touch with me directly. I can be reached by email, ehmatthes at gmail, or on twitter [@ehmatthes](https://twitter.com/ehmatthes).

If you would like to start contributing and aren't sure what to do, there is a list of places to start in [Issue 17](https://github.com/ehmatthes/intro_programming/issues/17).

On an Ubuntu system:
### Make a virtualenv with IPython for this project:
    $ mkdir /srv/intro_programming && cd intro_programming
    $ virtualenv --distribute venv
    $ source venv/bin/activate
    $ pip install ipython[all]
### Install pandoc, if you don't already have it installed:
    $ sudo apt-get install pandoc
### Clone this repository:
    $ git clone https://github.com/ehmatthes/intro_programming
### Open the notebooks:
    $ cd intro_programming/notebooks
    $ ipython notebook

This will open a browser, and you can click on the notebook you'd like to edit.

### Creating html versions of the notebooks:

    $ cd /srv/intro_programming/intro_programming/scripts
    $ ./create_common_html.sh

After this, you should see a .html file for each .ipynb file in the `notebooks` directory. These html files are ignored by git for this project. If you want to build your own custom site based off of this project, see `/scripts/modify_custom_html.sh` as well.

There may be a bit more involved in a full setup, depending on which versions of Python you have on your system, but that should get you up and running. If you have any questions about getting the project running locally, drop a note in [Issue 11](https://github.com/ehmatthes/intro_programming/issues/11), or get in touch with me directly. I can be reached by email, ehmatthes at gmail, or on twitter [@ehmatthes](https://twitter.com/ehmatthes).

Thanks for looking!

#### Chrome spacing bug
If you are seeing a bug when editing longer markdown cells, you may need to update your version of Chrome. There was a bug that caused extra spaces to build up behind the cursor when lines are wrapped in long markdown cells. A new version of Chrome fixed this issue. The default version of Chrome on 12.04 is 28 at this writing, so this is how I updated `chromium-browser` to version 29:

    sudo add-apt-repository ppa:chromium-daily/stable
    sudo apt-get update
    sudo apt-get dist-upgrade

Contributing - Detailed
---
These notebooks focus on Python 3.3, but they also show some Python 2.7 code. You may run into trouble working with the notebooks if you only have one version of Python, and one version of IPython Notebook on your system. This is how I set up my Ubuntu 12.04 system.

Add a ppa that has old and new versions of Python, and use the ppa to install Python 3.3

    sudo apt-get install python-software-properties
    sudo add-apt-repository ppa:fkrull/deadsnakes    
    sudo apt-get update    
    sudo apt-get install python3.3

[The rest of this is outdated - I will update this shortly with more up-to-date instructions.]
Install the correct versions of ipython, ipython-notebook, ipython3, and ipython3-notebook:

    sudo apt-get install ipython=0.13.2-1~ubuntu12.04.1
    sudo apt-get install ipython-notebook=0.13.2-1~ubuntu12.04.1
    sudo apt-get install ipython3=0.13.2-1~ubuntu12.04.1
    sudo apt-get install ipython3-notebook

- Now the command `ipython notebook` should start an IPython Notebook session with your system's standard version of Python.
- The command `ipython3-notebook` should start an IPython Notebook session using Python 3.3.
- I like to test which version of Python is being used with `print(3/2)`. If you Python 3.3 is being used, you will see `1.5`, and if Python 2.7 is being used you will see `1`.
- Again, if you are having trouble with any of this drop a note in [Issue 11](https://github.com/ehmatthes/intro_programming/issues/11), or feel free to get in touch directly.

Testing
---
(This part is current.) If you want to run test whether links in the notebooks are correct, you will need to install requests in your virtualenv.

    pip install requests
