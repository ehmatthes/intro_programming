# This script runs through all the html files in notebooks/, and 
#  modifies index.html links to ./
# Rationale:
#  ipynb files need to link to index notebook.
#  But html sites are better off linking to root, which will call index.html.
#  Calling index.html leads user to end up using two names for the index page,
#   which is confusing for tracking.

printf "\nConverting home links to ./ now...\n"

old_string="href='index.html'"
old_string_2='href="index.html"'
new_string="href='.\/'"

if [ -e "../notebooks/" ]
then
    find ../notebooks -iname '*.html' | xargs sed -i "s/$old_string/$new_string/"
    find ../notebooks -iname '*.html' | xargs sed -i "s/$old_string_2/$new_string/"
else
    find notebooks -iname '*.html' | xargs sed -i "s/$old_string/$new_string/"
    find notebooks -iname '*.html' | xargs sed -i "s/$old_string_2/$new_string/"
fi

printf "  Converted home links.\n"
