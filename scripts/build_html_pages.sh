#!/bin/bash

# This script builds the entire html page.
#  Assumes need to build from basic html, and construct custom-defined pages.
#
# When starting out, need to run a full nbconvert, and then pull out css and js
#  files into 'css' and 'js' directories, in the 'notebooks' dir. This is manual
#  right now, but it would be good to automate this and create a flag such as 
#  '--initial'.
#
# Starts by running 'ipython nbconvert --template basic'.
#   Then adds header sections and appropriate html page tags.
#   Script is meant to be fairly straightforward to modify, so users can 
#   build the static pages they care to make from the core notebooks.
#
# This is meant to work well through a post-commit-hook, although you can also
#  run the script manually when you want a snapshot of the notebooks in html
#  format.
#
# All html files are ignored by git.


if [ -e scripts/ ]
then
	 # Probably running as a commit hook.
    prefix="scripts/"
else
	 # Probably running directly from /scripts directory.
	 prefix=""
fi


# Build basic pages.
source "$prefix"create_common_html.sh
wait

# Create empty all_exercises_challenges page;
#   (Next scripts require a non-empty file at this point.)
printf "\n\nCreating empty all_exercises_challenges.html file..."
touch "$path_to_notebooks"/all_exercises_challenges.html
### DEV: This can probably be removed.
#echo "<br>" > "$prefix"/all_exercises_challenges.html
printf "\nCreated empty all_exercises_challenges.html file.\n\n"
wait
