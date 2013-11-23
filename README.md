A collection of IPython Notebooks for teaching Python.
---

Here is the [index page](http://www.introtopython.org), as students see the notebooks, and the [course syllabus](http://www.introtopython.org/syllabus.html). These are all static versions of the notebooks which have been converted to html, which are hosted at [introtopython.org](http://www.introtopython.org).

You can also view the raw notebooks using the IPython Notebook Viewer ([index page](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/index.ipynb), [course syllabus](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/syllabus.ipynb)). The content is almost identical on both sites, but the [introtopython.org](http://introtopython.org) version is easier to navigate, and has some dynamic js features such as collapsible output.

Contents
---
- [Goals](#goals)
- [Contributing - Brief](#contributing)
    - [Installing Python 3 on Ubuntu 12.04](#python3)
    - [Make a virtualenv with IPython](#virtualenv)
        - [Using requirements.txt](#requirements)
        - [Without using requirements.txt](#without_requirements)
    - [Creating html versions of the notebooks](#html)
    - [Editing Python 2.7 examples](#python2.7)
- [Contributing - Other](#contributing_other)

<a name='goals'></a>Goals:
---
- Introduce students as quickly as possible to the basics of programming, and then help them choose an interesting project that they are capable of completing.
- Introduce best practice as early as possible, while remaining accessible to students with no background in programming at all.

<a name='contributing'></a>Contributing - Brief:
---
Contributing to this project requires IPython version 1.1.0 or greater. These instructions are written based on setting up a development environment on Ubuntu 12.04, but they should be fairly adaptable to any modern system with a Python environment already set up. If you have any questions about getting your development environment set up for contributing to this project, please drop a note in [Issue 11](https://github.com/ehmatthes/intro_programming/issues/11), or get in touch with me directly. I can be reached by email, ehmatthes at gmail, or on twitter [@ehmatthes](https://twitter.com/ehmatthes).

If you would like to start contributing and aren't sure what to do, there is a list of places to start in [Issue 17](https://github.com/ehmatthes/intro_programming/issues/17).

These notebooks are written primarily in Python 3. If the default Python on your system is Python 3, then you will have a simpler time contributing to the project. If you only have Python 2, you might want to consider adding Python 3 to your system. You can contribute to the project using Python 2, since there is so much overlap between the two versions of Python, especially when working on the more basic notebooks. To fully contribute to the project, you will need to have both Python 2 and Python 3 available.

### <a name='python3'></a>Installing Python 3 on Ubuntu 12.04:
    $ sudo apt-get install python3.2
    $ sudo apt-get install python3.2-dev

One of the simplest differences between Python 2 and Python 3 is integer division. You can do a quick test to make sure both versions of Python are actually installed on your system:

    $ python3.2
    >>> 3/2
    1.5
    >>> exit()
    $ python2.7
    >>> 3/2
    1

### <a name='virtualenv'></a>Make a virtualenv with IPython for this project
The project includes a skeleton *requirements.txt* file to help you set up a virtualenv dedicated to this project. Using this file will install matplotlib, which is a fairly significant installation. If you want the full environment, use the *requirements.txt* file when you set up your virtualenv. If you don't want the full environment, you can set up your virtualenv manually. Both ways of setting up the project are included here.

#### Install pandoc
Pandoc is used by IPython Notebook to convert from the *.ipynb* format to *.html*.

    $ sudo apt-get install pandoc

#### <a name='requirements'></a>Using *requirements.txt*:
    $ mkdir /srv/intro_programming && cd intro_programming
    $ virtualenv -p python3.2 venv
    $ source venv/bin/activate
    $ git clone https://github.com/ehmatthes/intro_programming
    $ pip install -r intro_programming/requirements.txt

This could easily fail to fully install, because there are a lot of requirements for IPython and matplotlib. If you have any questions about the installation process, [please ask](https://github.com/ehmatthes/intro_programming/issues/11). I would like to help people get set up to contribute, so I will be happy to help troubleshoot setup issues.

#### <a name='without_requirements'></a>Without using *requirements.txt*:
    $ mkdir /srv/intro_programming && cd intro_programming
    $ virtualenv -p python3.2 venv
    $ source venv/bin/activate
    $ git clone https://github.com/ehmatthes/intro_programming
    $ pip install ipython[all]==1.1.0 # required to access the notebooks
    $ pip install requests==2.0.0 # required for testing links within the project
    $ pip install matplotlib==1.3.1 # only required for some notebooks

### Open the notebooks:
    $ cd intro_programming/notebooks
    $ ipython notebook

This will open a browser, and you can click on the notebook you'd like to edit.

### <a name='html'></a>Creating html versions of the notebooks:

    $ cd /srv/intro_programming/intro_programming/scripts
    $ ./build_html_pages

After this, you should see a .html file for each .ipynb file in the `notebooks` directory. These html files are ignored by git for this project. If you want to build your own custom site based off of this project, look at the source for `/scripts/build_html_pages.sh`. It should be fairly straightforward to see how the html pages are built, and you should be able to customize your own html output.

#### View your html pages
To view your html pages, you need to start a server in the intro_programming/notebooks directory, and then access the pages locally:

    $ cd /srv/intro_programming/intro_programming/notebooks
    $ python -m SimpleHTTPServer

Then go to [http://localhost:8000](http://localhost:8000), and you should see the index page. By the way, if you are using an index page with social plugins, you can see all the people who have accidentally tweeted or shared a local development version of their project. :)

### <a name='python2.7'></a>Editing Python 2.7 examples

To edit the Python 2 examples in some of the notebooks, it is helpful to have a separate virtualenv that is built using Python 2.7. The steps to set up this virtualenv are identical to the steps above, except

    $ mkdir /srv/intro_programming && cd intro_programming
    $ virtualenv -p python3.2 venv

becomes

    $ mkdir /srv/intro_programming2.7 && cd intro_programming2.7
    $ virtualenv -p python2.7 venv

There may be a bit more involved in a full setup, depending on which versions of Python you have on your system, but that should get you up and running. If you have any questions about getting the project running locally, drop a note in [Issue 11](https://github.com/ehmatthes/intro_programming/issues/11), or get in touch with me directly. I can be reached by email, ehmatthes at gmail, or on twitter [@ehmatthes](https://twitter.com/ehmatthes).

Thanks for looking!

### Chrome spacing bug
If you are seeing a bug when editing longer markdown cells, you may need to update your version of Chrome. There was a bug that caused extra spaces to build up behind the cursor when lines are wrapped in long markdown cells. A new version of Chrome fixed this issue. The default version of Chrome on 12.04 is 28 at this writing, so this is how I updated `chromium-browser` to version 29:

    sudo add-apt-repository ppa:chromium-daily/stable
    sudo apt-get update
    sudo apt-get dist-upgrade

<a name='contributing_other'></a>Contributing - Other
---
Ubuntu 12.04 has Python 2.7 and Python 3.2 available through the default repositories. If you want versions of Python that are not available through the default repositories, you can use the *deadsnakes* repository to install other versions:

    sudo apt-get install python-software-properties
    sudo add-apt-repository ppa:fkrull/deadsnakes    
    sudo apt-get update    
    sudo apt-get install python3.3
