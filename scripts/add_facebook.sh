# This script runs through all the html files in notebooks/, and adds in 
#  required code for the facebook button.
# Adds facebook js.

printf "\nAdding facebook button resources..."

# String right before where the new element should go.
before_string="<body>"
# String right after where the new element should go.
#after_string = ""

# String that should be added in.
new_string='<div id="fb-root"><\/div>\n'
new_string+='<script>(function(d, s, id) {\n'
new_string+='  var js, fjs = d.getElementsByTagName(s)[0];\n'
new_string+='  if (d.getElementById(id)) return;\n'
new_string+='  js = d.createElement(s); js.id = id;\n'
new_string+='  js.src = "\/\/connect.facebook.net\/en_US\/all.js#xfbml=1";\n'
new_string+='  fjs.parentNode.insertBefore(js, fjs);\n'
new_string+='}(document, "script", "facebook-jssdk"));<\/script>\n'


if [ -e "../notebooks/" ]
then
    find ../notebooks -iname '*.html' | xargs sed -i "s/$before_string/$before_string\n$new_string\n/"
else
    find notebooks -iname '*.html' | xargs sed -i "s/$before_string/$before_string\n$new_string\n/"
fi

printf "\nAdded facebook button resources.\n\n"




