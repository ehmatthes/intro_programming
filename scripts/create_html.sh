# This file converts all notebooks in the notebooks directory to html, for 
#  hosting on a static site.
# 
# The main work is to convert links properly, and insert any site-specific
#  html or javascript code that would otherwise clutter the notebooks.
#
# This is meant to make it easy for anyone to build a site focused on helping 
#  people learn to use Python.

# Do the raw conversion from .ipynb to .html
cd ../notebooks && ipython nbconvert *.ipynb

# Go through each html file, changing links from nbviewer basis to static html basis.
printf "\nConverting links to html..."
find ../notebooks -iname '*.html' | xargs sed -i 's/http:\/\/nbviewer.ipython.org\/urls\/raw.github.com\/ehmatthes\/intro_programming\/master\/notebooks\///g'
find ../notebooks -iname '*.html' | xargs sed -i 's/.ipynb/.html/g'
printf "\nFinished converting links.\n"

# Temporary fix, until intro_programming_index renamed, and links updated.
printf "\nCopying intro_programming_index.html to index.html..."
cp ../notebooks/intro_programming_index.html ../notebooks/index.html
printf "\nCopied file.\n"

# To insert Google Analytics code,
#   store it as "intro_programming/ignored_resources/ga_code.txt".
#   Newlines in GA code may throw errors; download or make a one-line version
#   of your GA code.
# Insert Google Analytics code just before </head>, if analytics code exists
printf "\nInserting Google Analytics code..."
if [ -e "../ignored_resources/ga_code.txt" ] ; then
    ga_code=$(<../ignored_resources/ga_code.txt)
    find ../notebooks -iname '*.html' | xargs sed -i "s#<\/head>#$ga_code\n<\/head>#g"
    printf "\nInserted analytics code.\n"
else
    printf "\nERROR - Couldn't find analytics code.\n"
fi
