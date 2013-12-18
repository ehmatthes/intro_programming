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
    # Probably running from a post-commit hook.

    # Build basic pages.
    source scripts/create_common_html.sh
    wait

	 # Create empty all_exercises_challenges page.
	 echo "Creating empty all_exercises_challenges.html file..."
	 touch notebooks/all_exercises_challenges.html
	 echo "\n" > notebooks/all_exercises_challenges.html
    echo "Created empty all_exercises_challenges.html file."
	 wait

    # Add opening tags
    source scripts/add_opening_tags.sh
    wait
    # Add title tag
    source scripts/add_title.sh
    wait
    # Add css and js links, and favicon link
    source scripts/add_css_js_links.sh
    wait
    # Close head and open body
    source scripts/close_head_open_body.sh
    wait
    # Close body and html tags.
    source scripts/close_body_html.sh
    # Add bootstrap.
    source scripts/add_bootstrap.sh
    wait

	 # If custom index file exists, overwrite index just created.
	 source scripts/copy_custom_index.sh
	 wait

	 # Customize all pages to use bootstrap
     #  Also adds navbar from index to all pages
	 printf "Customizing all styles to use bootstrap...\n"
	 python scripts/add_bootstrap.py
	 wait
	 printf "Customized styles.\n\n"

	 # Add elements to toggle output on each page.
	 printf "Adding ability to toggle output on each page...\n"
	 python scripts/show_hide_output.py
	 wait
	 printf "Added toggling ability.\n\n"

	 # Convert index.html links to ./
    source scripts/convert_home_links.sh
    wait

    # Add fb button.
    source scripts/add_facebook.sh
    wait
    python scripts/modify_facebook_urls.py
    wait

	 # Convert image links from ipynb format to html.
	 source scripts/convert_image_links.sh
	 wait

	 # Highlight lines of code.
	 python scripts/highlight_code.py
	 wait

	 # Create page containing all exercises and challenges.
	 python scripts/build_all_exercises_page.py
	 wait

    # Insert Google Analytics code.
	 #  This should happen last, so that ga code is just before
	 #  closing head tag.
    source scripts/insert_google_analytics.sh
	 wait

else
    # Probably running this script directly, from scripts/ dir.

    # Build basic pages.
    source create_common_html.sh
    wait

	 # Create empty all_exercises_challenges page.
	 echo "Creating empty all_exercises_challenges.html file..."
	 touch ../notebooks/all_exercises_challenges.html
	 echo "\n" > ../notebooks/all_exercises_challenges.html
    echo "Created empty all_exercises_challenges.html file."
	 wait

    # Add opening tags
    source add_opening_tags.sh
    wait
    # Add title tag
    source add_title.sh
    wait
    # Add css and js links, and favicon link
    source add_css_js_links.sh
    wait
    # Close head and open body
    source close_head_open_body.sh
    wait
    # Close body and html tags.
    source close_body_html.sh
    wait
    # Add bootstrap.
    source add_bootstrap.sh
    wait

	 # If custom index file exists, overwrite index just created.
	 source copy_custom_index.sh
	 wait

	 # Customize all pages to use bootstrap
     #  Also adds navbar from index to all pages
	 printf "Customizing all styles to use bootstrap...\n"
	 python add_bootstrap.py
	 wait
	 printf "Customized styles.\n\n"

	 # Add elements to toggle output on each page.
	 printf "Adding ability to toggle output on each page...\n"
	 python show_hide_output.py
	 wait
	 printf "Added toggling ability.\n\n"

	 # Convert index.html links to ./
    source convert_home_links.sh
    wait

    # Add fb button.
    source add_facebook.sh
    wait
    python modify_facebook_urls.py
    wait

	 # Convert image links from ipynb format to html.
	 source convert_image_links.sh
	 wait

	 # Highlight lines of code.
	 python highlight_code.py
	 wait

	 # Create page containing all exercises and challenges.
	 python build_all_exercises_page.py
	 wait

    # Insert Google Analytics code.
	 #  This should happen last, so that ga code is just before
	 #  closing head tag.
    source insert_google_analytics.sh
	 wait

fi


printf "\n\n"
