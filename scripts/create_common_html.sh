#!/bin/bash
#
# This file converts all notebooks in the notebooks directory to html, for 
#  hosting on a static site.
#
# This script converts all notebooks from IPython Notebook
#  syntax to raw html. It then converts all internal links to point to
#  these html documents rather than documents served from
#  the IPython Notebook Viewer.
#
# All conversion steps that are particular to an individual deployment of the 
#  static html files are done separately, in modify_custom_html.sh.
#
# This is meant to make it easy for anyone to build a simple static site
#  focused on helping people learn to use Python.
#
# This code is meant to work well as a post-commit hook. That way the html files
#  are kept up to date with the raw notebooks. However, this script can be run
#  manually when you want an html snapshot of the notebooks.
#
# All html files are ignored by git.


# Sometimes this file is run on its own (from this directory),
#  sometimes from a post-commit hook (from another directory).
#  The if structure lets it run either way.
# This could be cleaned up, perhaps by setting the correct path to notebooks in
#  an if clause, and then running the code.
#
printf "\nConverting internal links to html..."
if [ -e ../notebooks ] ; then

    # Must be running directly, use ../notebooks path.
    printf "\nUsing ../notebooks path.\n"

    # Convert raw .ipynb files to raw .html files.
    printf "\nConverting raw .ipynb files to raw .html files..."
    cd ../notebooks && ipython nbconvert *.ipynb
    printf "\nFinished converting files.\n"

    # Go through each html file, changing all internal links so they point to these
    #  raw html files, rather than IPython Notebook Viewer files.
    printf "\nConverting internal links to point to html files..."
    find ../notebooks -iname '*.html' | xargs sed -i 's/http:\/\/nbviewer.ipython.org\/urls\/raw.github.com\/ehmatthes\/intro_programming\/master\/notebooks\///g'
    find ../notebooks -iname '*.html' | xargs sed -i 's/.ipynb/.html/g'
    printf "\nFinished converting links.\n"

    # Temporary fix, until intro_programming_index renamed, and links updated.
    printf "\nCopying intro_programming_index.html to index.html..."
    cp ../notebooks/intro_programming_index.html ../notebooks/index.html
    printf "\nCopied file.\n"

else

    # Must be running from a pre-commit hook, which has a different path
    #  to the notebooks directory for some commands.
    printf "\nUsing notebooks path.\n"

    # Convert raw .ipynb files to raw .html files.
    printf "\nConverting raw .ipynb files to raw .html files..."
    cd notebooks && ipython nbconvert *.ipynb
    printf "\nFinished converting files.\n"

    # Go through each html file, changing all internal links so they point to these
    #  raw html files, rather than IPython Notebook Viewer files.
    printf "\nConverting internal links to point to html files..."
    find ../notebooks -iname '*.html' | xargs sed -i 's/http:\/\/nbviewer.ipython.org\/urls\/raw.github.com\/ehmatthes\/intro_programming\/master\/notebooks\///g'
    find ../notebooks -iname '*.html' | xargs sed -i 's/.ipynb/.html/g'
    printf "\nFinished converting links.\n"

    # Temporary fix, until intro_programming_index renamed, and links updated.
    printf "\nCopying intro_programming_index.html to index.html..."
    cp ../notebooks/intro_programming_index.html ../notebooks/index.html
    printf "\nCopied file.\n"

fi
