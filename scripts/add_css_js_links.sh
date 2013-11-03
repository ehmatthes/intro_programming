# This file adds necessary css and js links to each page.
#
# Should be the collection of links that are needed.


printf "\nAdding css and js links to html files..."

# String right before where the title should be
before_string='<\/title>'

# ipynb styles, and my overrides
css_js_link_string="<link rel='stylesheet' href='css\/nbconvert_styles.css'>\n"
css_js_link_string="$css_js_link_string<link rel='stylesheet' href='css\/nb_overrides.css'>\n"

# custom site styles
css_js_link_string="$css_js_link_string<link rel='stylesheet' href='css\/site_styles.css'>\n"

# jquery, included here rather than at end of page ala bootstrap,
#  so I can access it for toggling elements.
css_js_link_string="$css_js_link_string<script src='js\/jquery.js'><\/script>\n"

# mathjax, and ipynb js
css_js_link_string="$css_js_link_string<script src='https:\/\/c328740.ssl.cf1.rackcdn.com\/mathjax\/latest\/MathJax.js?config=TeX-AMS_HTML' type='text\/javascript'><\/script>\n"
css_js_link_string="$css_js_link_string<script type='text\/javascript' src='js\/nbconvert_js.js'><\/script>\n"

# js file to show/ hide output
css_js_link_string="$css_js_link_string<script type='text\/javascript' src='js\/show_hide_output.js'><\/script>\n"
printf "HERE HERE HERE\n"
printf "css_js $css_js_link_string\n"

# Not using this at this point, just leads to unfound resource.
#css_js_link_string="$css_js_link_string<!-- Custom stylesheet, it must be in the same directory as the html file -->\n"
#css_js_link_string="$css_js_link_string<link rel='stylesheet' href='custom.css'>\n"



if [ -e "../notebooks/" ]
then
    find ../notebooks -iname '*.html' | xargs sed -i "s/$before_string/$before_string\n\n$css_js_link_string\n/"
else
    find notebooks -iname '*.html' | xargs sed -i "s/$before_string/$before_string\n\n$css_js_link_string\n/"
fi

printf "\nAdded css and js links.\n\n"
