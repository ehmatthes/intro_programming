# If a custom index page exists, this script copies that file to the 
#  notebooks directory, and overwrites that automatically-generated
#  index.html page.

printf "\nCopying custom index.html page..."

if [ -e "../notebooks/" ]
then
	 cp ../html_resources/index.html ../notebooks/index.html
else
	 cp html_resources/index.html notebooks/index.html
fi

if [ $? == 0 ]
then
	 printf "\nCopied custom index.html page.\n\n"
else
	 printf "\nCouldn't find custom index.html page.\n\n"
fi
