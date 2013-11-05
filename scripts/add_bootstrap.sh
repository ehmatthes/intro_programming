# This script runs through all the html files in notebooks/, and adds in 
#  bootstrap tags where appropriate.

printf "\nAdding link to bootstrap resources."

# String right before where the new element should go.
before_string=""
# String right after where the new element should go.
after_string="<\/head>"

# String that should be added in.
new_string="<link href='css\/bootstrap.css' rel='stylesheet' media='screen'>\n"
#new_string+="<link href='jumbotron-narrow.css' rel='stylesheet'>\n"
new_string+="<link href='css\/non-responsive.css' rel='stylesheet'>\n"

# Leaving this line in makes for responsive site, but then code blocks get mangled on mobile.
#  May put this back in if just code blocks can be made non-responsive.
#new_string+="<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
new_string+="<link href='css\/bootstrap_overrides.css' rel='stylesheet'>"


if [ -e "../notebooks/" ]
then
    find ../notebooks -iname '*.html' | xargs sed -i "s/$after_string/$new_string\n$after_string\n/"
else
    find notebooks -iname '*.html' | xargs sed -i "s/$after_string/$new_string\n$after_string\n/"
fi

printf "\nAdded link to bootsrap resources.\n"


# ----- Add overall bootstrap container to page -----
printf "\nAdding bootstrap to html files..."

# String right before where the new element should go.
before_string="<body>"
# String right after where the new element should go.
after_string=""

# String that should be added in.
new_string="<div class='container'>"

if [ -e "../notebooks/" ]
then
    find ../notebooks -iname '*.html' | xargs sed -i "s/$before_string/$before_string\n$new_string/"
else
    find notebooks -iname '*.html' | xargs sed -i "s/$before_string/$before_string\n$new_string/"
fi

# String right before where the new element should go.
before_string=""
# String right after where the new element should go.
after_string="<\/body>"

# String that should be added in.
new_string="<\/div>"

if [ -e "../notebooks/" ]
then
    find ../notebooks -iname '*.html' | xargs sed -i "s/$after_string/$new_string\n$after_string\n/"
else
    find notebooks -iname '*.html' | xargs sed -i "s/$after_string/$new_string\n$after_string\n/"
fi



printf "\nAdded bootstrap.\n\n"
