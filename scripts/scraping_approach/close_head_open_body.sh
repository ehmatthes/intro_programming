# Closes the head section and opens the body.


printf "\nAdding closing head tag and opening body tag..."

# String right before where the title should be
#before_string="<script type='text\/javascript' src='js\/nbconvert_js.js'><\/script>"
before_string="<script type='text\/javascript' src='js\/show_hide_output.js'><\/script>"
head_body_tags_string="<\/head>\n<body>"



if [ -e "../notebooks/" ]
then
    find ../notebooks -iname '*.html' | xargs sed -i "s/$before_string/$before_string\n$head_body_tags_string\n/"
else
    find notebooks -iname '*.html' | xargs sed -i "s/$before_string/$before_string\n$head_body_tags_string\n/"
fi

printf "\nAdded closing head tag and opening body tag.\n\n"
