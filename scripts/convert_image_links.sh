# This script runs through all the html files in notebooks/, and 
#  modifies image links from files/images/filename to
#  images/filename.
# Rationale:
#  IPython Notebook needs the word 'files' prepended to any file paths,
#  and html does not.

printf "Removing 'files/' from image links...\n"

old_string="files\/images\/"
new_string="images\/"

if [ -e "../notebooks/" ]
then
    find ../notebooks -iname '*.html' | xargs sed -i "s/$old_string/$new_string/"
else
    find notebooks -iname '*.html' | xargs sed -i "s/$old_string/$new_string/"
fi

printf "Removed 'files/' from image links.\n"