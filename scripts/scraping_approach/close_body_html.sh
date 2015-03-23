# This file adds the closing body and html tags to the end of the file.
#

printf "\nAdding closing body and closing html tags to ends of html files..."

if [ -e "../notebooks/" ]
then
    find ../notebooks -iname '*.html' | xargs sed -i '$a\</body>\n</html>'
else
    find notebooks -iname '*.html' | xargs sed -i '$a\</body>\n</html>'
fi

printf "\nAdded closing tags.\n\n"
