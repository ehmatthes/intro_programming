# To insert Google Analytics code,
#   store it as "intro_programming/ignored_resources/ga_code.txt".
#   Newlines in GA code may throw errors; download or make a one-line version
#   of your GA code.
#
# Insert Google Analytics code just before </head>, if analytics code exists
printf "\nInserting Google Analytics code..."

if [ -e "../ignored_resources/ga_code.txt" ] ; then
    ga_code=$(<../ignored_resources/ga_code.txt)
    find ../notebooks -iname '*.html' | xargs sed -i "s#<\/head>#$ga_code\n<\/head>\n#g"
    printf "\nInserted analytics code.\n"

else
    ga_code=$(<ignored_resources/ga_code.txt)
    find notebooks -iname '*.html' | xargs sed -i "s#<\/head>#$ga_code\n<\/head>\n#g"
    printf "\nInserted analytics code.\n"

fi
