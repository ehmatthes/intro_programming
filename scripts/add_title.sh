# This file adds a title to each html page.
#
# Should pull title from the top of each page.
#  Good place would be the first content within an h1 tag.
#  For now, just title everything 'Introduction to Python'.


printf "\nAdding titles to html files..."

# String right before where the title should be
before_string="<meta charset='UTF-8'>"
title_string='<title>Introduction to Python<\/title>\n'

if [ -e "../notebooks/" ]
then
    find ../notebooks -iname '*.html' | xargs sed -i "s/$before_string/$before_string\n\n$title_string/"
else
    find notebooks -iname '*.html' | xargs sed -i "s/$before_string/$before_string\n\n$title_string/"
fi

printf "\nAdded titles.\n\n"
