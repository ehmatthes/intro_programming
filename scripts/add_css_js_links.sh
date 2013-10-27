# This file adds necessary css and js links to each page.
#
# Should be the collection of links that are needed.


printf "\nAdding css and js links to html files..."

# String right before where the title should be
before_string='<\/title>'

css_js_link_string="<link rel='stylesheet' href='css\/nbconvert_styles.css'>\n"
css_js_link_string="$css_js_link_string<script type='text\/javascript' src='js\/nbconvert_js.js'><\/script>\n"
css_js_link_string="$css_js_link_string<!-- Custom stylesheet, it must be in the same directory as the html file -->\n"
css_js_link_string="$css_js_link_string<link rel='stylesheet' href='custom.css'>\n"



if [ -e "../notebooks/" ]
then
    find ../notebooks -iname '*.html' | xargs sed -i "s/$before_string/$before_string\n\n$css_js_link_string\n/"
else
    find notebooks -iname '*.html' | xargs sed -i "s/$before_string/$before_string\n\n$css_js_link_string\n/"
fi

printf "\nAdded css and js links.\n\n"
