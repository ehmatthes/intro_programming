# This file makes modifications to the html files that are common to every
#  deployment involving static files.
#
# For now this is focused on inserting analytics code, but it will also be about
#  adding headers, footers, and any other custom html desired.
#
# This is meant to work well through a post-commit-hook, although you can also
#  run the script manually when you want a snapshot of the notebooks in html
#  format.
#
# All html files are ignored by git.


# To insert Google Analytics code,
#   store it as "intro_programming/ignored_resources/ga_code.txt".
#   Newlines in GA code may throw errors; download or make a one-line version
#   of your GA code.
#
# Insert Google Analytics code just before </head>, if analytics code exists
printf "\nInserting Google Analytics code..."
if [ -e "../ignored_resources/ga_code.txt" ] ; then
    ga_code=$(<../ignored_resources/ga_code.txt)
    find ../notebooks -iname '*.html' | xargs sed -i "s#<\/head>#$ga_code\n<\/head>#g"
    printf "\nInserted analytics code.\n"
else
    ga_code=$(<ignored_resources/ga_code.txt)
    find notebooks -iname '*.html' | xargs sed -i "s#<\/head>#$ga_code\n<\/head>#g"
    printf "\nInserted analytics code.\n"
fi
