# This script runs through all the html files in notebooks/, and 
#  modifies <code> tags to <code class="inline_code">
# Rationale:
#  Inline code blocks are much easier to recognize when they are highlighted,
#  in a manner similar to stackoverflow.

printf "\nHighlighting inline code blocks...\n"

old_string='<code>'
new_string='<code class="inline_code">'

if [ -e "../notebooks/" ]
then
    find ../notebooks -iname '*.html' | xargs sed -i "s/$old_string/$new_string/g"
else
    find notebooks -iname '*.html' | xargs sed -i "s/$old_string/$new_string/g"
fi


printf "  Highlighted inline code blocks.\n"
