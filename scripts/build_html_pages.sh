#!/bin/bash

# This script builds the entire html page.
#  Assumes need to build from basic html, and construct custom-defined pages.
#
# When starting out, need to run a full nbconvert, and then pull out css and js
#  files into 'css' and 'js' directories, in the 'notebooks' dir. This is manual
#  right now, but it would be good to automate this and create a flag such as 
#  '--initial'.
#
# Starts by running 'ipython nbconver --template basic'.
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
    # Probably running from a post-commit hook.

    # Build basic pages.
    source scripts/create_common_html.sh
    wait

    # Insert Google Analytics code.
    source scripts/insert_google_analytics.sh

else
    # Probably running this script directly, from scripts/ dir.

    # Build basic pages.
    source create_common_html.sh
    wait


    # Insert Google Analytics code.
    source insert_google_analytics.sh

fi


printf "\n\n"
