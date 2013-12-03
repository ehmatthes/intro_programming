# This script runs through all the html files in notebooks/, and 
#  converts `highlight=[1,2, 5-10]` directives to style directives
#  for highlighting lines of code in code cells.

import os, sys
import ast

print("Highlighting code...")

# Find all files to work with.
path_to_notebooks = '/srv/projects/intro_programming/intro_programming/notebooks/'
filenames = []
for filename in os.listdir(path_to_notebooks):
    if '.html' in filename and filename != 'index.html':
        filenames.append(filename)

# one file for testing:
filenames = ['visualization_earthquakes.html']



for filename in filenames:

    f = open(path_to_notebooks + filename, 'r')
    lines = f.readlines()
    f.close()

    f = open(path_to_notebooks + filename, 'wb')
    for line in lines: 
        if '###highlight' in line:
            print('here')
            # Get lines to highlight, stored as a list.
            #  Lines are in a list, after the equals sign.
            print(line[line.index('highlight=')+10:line.index(']')+1])
            highlight_lines = ast.literal_eval(line[line.index('highlight=')+10:line.index(']')+1])
            print(highlight_lines)
        f.write(line.encode('utf-8'))


        #if old_fb_url in line:
            #new_line = line.replace(old_fb_url, new_fb_url)
            #f.write(new_line.encode('utf-8'))
        #else:
            #f.write(line.encode('utf-8'))
    f.close()


print("Highlighted code.\n")


