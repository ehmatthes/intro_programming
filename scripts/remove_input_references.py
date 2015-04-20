# This script removes the input reference numbers from html pages.
#  They play a useful role in scientific notebooks, but they are really
#  just visual clutter in this project.
# Could be an nbconvert setting, but it's an easy enough scripting job.

import os
import sys

print("\nStripping input reference numbers from code cells...")

# Find all files to work with.
path_to_notebooks = '/srv/projects/intro_programming/intro_programming/notebooks/'
filenames = []
for filename in os.listdir(path_to_notebooks):
    if '.html' in filename and filename != 'index.html':
        filenames.append(filename)

# one file for testing:
#filenames = ['hello_world.html']

for filename in filenames:

    f = open(path_to_notebooks + filename, 'r')
    lines = f.readlines()
    f.close()

    f = open(path_to_notebooks + filename, 'wb')
    for line in lines: 
        # Unwanted lines have opening and closing div on same line,
        #  with input reference number between them.
        if ('<div class="prompt input_prompt">' in line 
                and '</div>' in line):
            # Don't write this line.
            continue
        else:
            # Regular line, write it.
            f.write(line.encode('utf-8'))
                
    f.close()

print("  Stripped input reference numbers.\n")

