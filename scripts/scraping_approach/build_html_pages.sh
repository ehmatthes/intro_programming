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

# Create empty all_exercises_challenges page.
# Next scripts require a non-empty file at this point.
echo "Creating empty all_exercises_challenges.html file..."
if [ -e notebooks/ ]
then
	 touch notebooks/all_exercises_challenges.html
	 echo "<br>" > notebooks/all_exercises_challenges.html
else
	 touch ../notebooks/all_exercises_challenges.html
	 echo "<br>" > ../notebooks/all_exercises_challenges.html
fi
echo "Created empty all_exercises_challenges.html file."
wait

# Add opening tags
source "$prefix"add_opening_tags.sh
wait

# Add title tag
source "$prefix"add_title.sh
wait

# Add css and js links, and favicon link
source "$prefix"add_css_js_links.sh
wait

# Close head and open body
source "$prefix"close_head_open_body.sh
wait

# Close body and html tags.
source "$prefix"close_body_html.sh
wait

# Create page containing all exercises and challenges.
#  This page needs to be created before bootstrap is added.
python "$prefix"build_all_exercises_page.py
wait

# Add bootstrap.
source "$prefix"add_bootstrap.sh
wait

# If custom index file exists, overwrite index just created.
source "$prefix"copy_custom_index.sh
wait

# Customize all pages to use bootstrap
#  Also adds navbar from index to all pages
printf "Customizing all styles to use bootstrap...\n"
python "$prefix"add_bootstrap.py
wait
printf "Customized styles.\n\n"

# Add elements to toggle output on each page.
printf "Adding ability to toggle output on each page...\n"
python "$prefix"show_hide_output.py
wait
printf "Added toggling ability.\n\n"

# Convert index.html links to ./
source "$prefix"convert_home_links.sh
wait

# Add fb button.
source "$prefix"add_facebook.sh
wait
python "$prefix"modify_facebook_urls.py
wait

# Convert image links from ipynb format to html.
source "$prefix"convert_image_links.sh
wait

# Highlight lines of code.
python "$prefix"highlight_code.py
wait

# Highlight inline blocks of code.
source "$prefix"highlight_inline_code.sh
wait

# Strip input references from code cells.
python "$prefix"remove_input_references.py
wait

# Insert Google Analytics code.
#  This should happen last, so that ga code is just before
#  closing head tag.
source "$prefix"insert_google_analytics.sh
wait

printf "\n\n"
