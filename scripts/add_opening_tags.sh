# This file adds the first few tags that need to appear on every html page.
#
# DOCTYPE declaration
# opens html tag
# opens head tag
# meta charset tag

opening_tags="<!DOCTYPE html>\n<html>\n<head>\n<meta charset='UTF-8'>\n"

printf "\nAdding opening tags to html files..."

if [ -e "../notebooks/" ]
then
    find ../notebooks -iname '*.html' | xargs sed -i "1s/^/$opening_tags/"
else
    find notebooks -iname '*.html' | xargs sed -i "1s/^/$opening_tags/"
fi

printf "\nAdded opening tags.\n\n"
