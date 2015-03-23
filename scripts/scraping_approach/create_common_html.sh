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

# Arguments
#  --full, -f
#      The script assumes you have the css files pulled out separately,
#        so that it can just write out basic html files.
#      This flag makes the script write out the full html file using
#        nbconvert. The first time you run this file, use this flag.
#        Then pull the css into a separate folder, and run the
#        modify_custom_html.sh script, so that it writes a header that 
#        includes a link to your css file.

for var in $@
do
    if [ $var == '--full' ] || [ $var == '-f' ]
    then
		  run_full_conversion=true
    fi
done

if [ $run_full_conversion ]
then
	 printf "\nRunning full conversion to html...\n"
else
	 printf "\nRunning basic conversion to html...\n"
fi


# Store current path, to return to at end of script
execution_path=$PWD


printf "\nConverting internal links to html..."
if [ -e ../notebooks ] ; then

    # Must be running directly, use ../notebooks path.
    printf "\nUsing ../notebooks path.\n"

    # Remove old html files.
    printf "\nRemoving old html files..."
    rm ../notebooks/*.html
    printf "\n  Removed files."

    # Convert raw .ipynb files to raw .html files.
    printf "\nConverting raw .ipynb files to raw .html files..."
	 if [ $run_full_conversion ]
		  then
		      cd ../notebooks && ipython nbconvert *.ipynb
		  else
		      cd ../notebooks && ipython nbconvert --template basic *.ipynb
	 fi

    printf "\n  Converted files.\n"

    # Go through each html file, changing all internal links so they point to these
    #  raw html files, rather than IPython Notebook Viewer files.
    printf "\nConverting internal links to point to html files..."
    find ../notebooks -iname '*.html' | xargs sed -i 's/http:\/\/nbviewer.ipython.org\/urls\/raw.github.com\/ehmatthes\/intro_programming\/master\/notebooks\///g'
    find ../notebooks -iname '*.html' | xargs sed -i 's/.ipynb/.html/g'
    printf "\n  Converted links.\n"

else

    # Must be running from a post-commit hook, which has a different path
    #  to the notebooks directory for some commands.
    printf "\nUsing notebooks path.\n"

    # Remove old html versions
    printf "\nRemoving old html files..."
    rm notebooks/*.html
    printf "\n  Removed files.\n."

    # Convert raw .ipynb files to raw .html files.
    printf "\nConverting raw .ipynb files to raw .html files..."
	 if [ $run_full_conversion ]
		  then
		      cd notebooks && ipython nbconvert *.ipynb
		  else
		      cd notebooks && ipython nbconvert --template basic *.ipynb
	 fi

    printf "\n  Converted files.\n"

    # Go through each html file, changing all internal links so they point to these
    #  raw html files, rather than IPython Notebook Viewer files.
    printf "\nConverting internal links to point to html files..."
    find ../notebooks -iname '*.html' | xargs sed -i 's/http:\/\/nbviewer.ipython.org\/urls\/raw.github.com\/ehmatthes\/intro_programming\/master\/notebooks\///g'
    find ../notebooks -iname '*.html' | xargs sed -i 's/.ipynb/.html/g'
    printf "\nConverted links.\n"

fi


# Return to original directory, so calling script's working dir does not change.
cd $execution_path
