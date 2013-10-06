import os

# This will probably end up being a bash script. I thought I'd want to do some
#  Python stuff in here, but if it ends up being all os calls I'll just make it
#  a bash script.

# This file converts all notebooks in the notebooks directory to html, for 
#  hosting on a static site.
# 
# The main work is to convert links properly, and insert any site-specific
#  html or javascript code that would otherwise clutter the notebooks.
#
# This is meant to be easy for anyone to build a site focused on helping 
#  people learn to use Python.

# Do the raw conversion:
os.system("cd ../notebooks && ipython nbconvert *.ipynb")

# Go through each file, changing links from nbviewer basis to static html basis.
print "\nConverting links to html..."
os.system("find ../notebooks -iname '*.html' | xargs sed -i 's/http:\/\/nbviewer.ipython.org\/urls\/raw.github.com\/ehmatthes\/intro_programming\/master\/notebooks\///g'")
os.system("find ../notebooks -iname '*.html' | xargs sed -i 's/.ipynb/.html/g'")
print "\nFinished converting links."
