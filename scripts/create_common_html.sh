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

printf "\nRunning initial conversion to html...\n"

# Store current path, to return to at end of script
execution_path=$PWD

# Set correct path:
if [ -e ../notebooks ]
then
	 # Must be running directly from /scripts directory.
	 path_to_notebooks="../notebooks"
else
	 # Probably running from a post-commit hook, probably from
	 #  root project directory.
	 path_to_notebooks="notebooks"
fi

# Remove old html files.
printf "\nRemoving old html files..."
rm "$path_to_notebooks"/*.html
printf "$path_to_notebooks"/*.html
printf "\n  Removed files."

# Convert raw .ipynb files to raw .html files.
### DEV: This is where templates should be introduced.
###   Then I can remove some of the other build scripts, and
###   diagnose changes in styling issues.
printf "\nConverting raw .ipynb files to raw .html files...\n"
cd "$path_to_notebooks" && ipython nbconvert --template my_templates/intro_python_base.tpl *.ipynb
printf "\n  Converted files.\n"

# Go through each html file, changing all internal links so they point to these
#  raw html files, rather than IPython Notebook Viewer files.
printf "\nConverting internal links to point to html files..."
find "$path_to_notebooks" -iname '*.html' | xargs sed -i 's/http:\/\/nbviewer.ipython.org\/urls\/raw.github.com\/ehmatthes\/intro_programming\/master\/notebooks\///g'
find "$path_to_notebooks" -iname '*.html' | xargs sed -i 's/.ipynb/.html/g'
printf "\n  Converted links.\n"

# Return to original directory, so calling script's working dir does not change.
cd $execution_path
