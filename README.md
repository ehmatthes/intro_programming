A collection of IPython Notebooks for teaching Python.
---

This project is the basis of [introtopython.org](http://introtopython.org), an open resource for teaching and learning Python. The site teaches the basics of Python, and then teaches people to build projects in Python. If you know how to work with IPython notebooks, you can contribute to the project.

You can also view the raw notebooks using the IPython Notebook Viewer ([home page](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/index.ipynb). The content is almost identical on both sites, but the [introtopython.org](http://introtopython.org) version is easier to navigate, and has some dynamic js features such as collapsible output.

Contents
---
- [Goals](#goals)
- [Contributing - Brief](#contributing)
    - [Using Miniconda to set up a development environment](#miniconda)
    - [Using virtualenv to set up a development environment](#virtualenv)
    - [Open the notebooks](#open_notebooks)
    - [Creating html versions of the notebooks](#html)
    - [Editing Python 2.7 examples](#python2.7)
    - [Questions](#questions)

<a name='goals'></a>Goals:
---
- Introduce students as quickly as possible to the basics of programming, and then help them choose an interesting project that they're capable of completing.
- Introduce best practice as early as possible, while remaining accessible to students with no background in programming at all.
- Help teachers who know little about programming start teaching Python to their students.
- Make it easy for experienced Python programmers to conduct a code review of the project.

<a name='contributing'></a>Contributing - Brief:
---
Contributing to this project requires IPython version 3.0 or higher. These instructions are written based on setting up a development environment on Ubuntu 14.04, but they should be adaptable to any modern system with a Python environment already set up. If you have any questions about getting your development environment set up for contributing to this project, please drop a note in [Issue 11](https://github.com/ehmatthes/intro_programming/issues/11), or get in touch with me directly. I can be reached by email, ehmatthes at gmail, or on twitter [@ehmatthes](https://twitter.com/ehmatthes).

If you would like to start contributing and aren't sure what to do, there is a list of places to start in [Issue 17](https://github.com/ehmatthes/intro_programming/issues/17).

These notebooks are written primarily in Python 3. If the default Python on your system is Python 3, then you'll have a simpler time contributing to the project. If you only have Python 2, you might want to consider adding Python 3 to your system. You can contribute to the project using Python 2, since there is so much overlap between the two versions of Python, especially when working on the more basic notebooks. To fully contribute to the project, you will need to have both Python 2 and Python 3 available.

### <a name="miniconda"></a>Using Miniconda to set up a development environment

The first visualization project ([Mapping Global Earthquake Activity](http://introtopython.org/visualization_earthquakes)) uses packages that are most conveniently installed using Conda.

The easiest way to do this is using Miniconda. Go to the [Miniconda home page](http://conda.pydata.org/miniconda.html). Download and run the appropriate installer for your system. The following commands will get conda set up on a 32-bit Linux system:

    ~$ wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86.sh
    ~$ bash Miniconda3-latest-Linux-x86.sh
    ~$   # Say yes to the prompt for prepending Miniconda3 install location to PATH
    ~$ exec bash

#### Create a conda environment
Once you've got conda installed, use it to make an environment for this project. Make a directory for this project, and start a conda environment that includes ipython and ipython notebook:

    $ mkdir introprogramming && cd introprogramming
    intro_programming$ conda create -n ip_env python=3 ipython ipython-notebook
    intro_programming$ source activate ip_env
    (ip_env)intro_programming$ 

From this point, the project works the same as using virtualenv. Skip ahead to [Open the notebooks](#open_notebooks)

### <a name='virtualenv'></a>Using virtualenv to set up a development environment
You can also use virtualenv to set up a development environment.

#### Install pandoc
Pandoc is used by IPython Notebook to convert from the *.ipynb* format to *.html*.

    $ sudo apt-get install pandoc

Now we'll set up the virtualenv:

    $ mkdir intro_programming && cd intro_programming
    intro_programming$ virtualenv -p python3 venv
    intro_programming$ source venv/bin/activate
    (venv)intro_programming$ git clone https://github.com/ehmatthes/intro_programming

    # Required to access the notebooks:
    (venv)intro_programming$ pip install ipython[all]==3 jsonschema

    # Required for testing links within the project:
    (venv)intro_programming$ pip install requests==2.0.0

### <a name="open_notebooks"></a>Open the notebooks:
    (venv)intro_programming$ cd intro_programming/notebooks
    (venv)intro_programming/intro_programming/notebooks$ ipython notebook

This will open a browser, and you can click on the notebook you'd like to edit.

#### <a name='html'></a>Creating html versions of the notebooks:

    (venv)intro_programming$ cd intro_programming/scripts
    (venv)intro_programming/intro_programming/scripts$ ./build_html_pages

After this, you should see an .html file for each .ipynb file in the `notebooks` directory. The html files are ignored by git for this project. If you want to build your own custom site based off this project, look at the source for `/scripts/build_html_pages.sh`. If you're not sure how to modify the script for your own purposes, I'm happy to help clarify how the conversion process works.

#### View your html pages
To view your html pages, start a server in the intro_programming/notebooks directory, and then access the pages locally:

    (venv)intro_programming$ cd intro_programming/notebooks
    (venv)intro_programming/intro_programming/notebooks$ python -m http.server

Then go to [http://localhost:8000](http://localhost:8000), and you should see the index page. (By the way, if you're using an index page with social plugins, you can see all the people who have accidentally tweeted or shared a local development version of their project. :)

### <a name='python2.7'></a>Editing Python 2.7 examples

To edit the Python 2 examples in some of the notebooks, it's helpful to have a separate virtualenv that is built using Python 2.7. The steps to set up this virtualenv are identical to the steps above, except

    $ mkdir intro_programming && cd intro_programming
    intro_programming$ virtualenv -p python3 venv

becomes

    $ mkdir intro_programming2.7 && cd intro_programming2.7
    intro_programming2.7$ virtualenv -p python2.7 venv

There may be a bit more involved in a full setup, depending on which versions of Python you have on your system, but that should get you up and running.

### <a name="questions"></a>Questions
If you have any questions about getting the project running locally, drop a note in [Issue 11](https://github.com/ehmatthes/intro_programming/issues/11), or get in touch with me directly. I can be reached by email, ehmatthes at gmail, or on twitter [@ehmatthes](https://twitter.com/ehmatthes).

Thanks for looking!
