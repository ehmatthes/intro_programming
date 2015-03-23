# This script removes the input reference numbers from html pages.
#  They play a useful role in scientific notebooks, but they are really
#  just visual clutter in this project.
# Could be an nbconvert setting, but it's an easy enough scripting job.

import os
import sys

print("Stripping input reference numbers from code cells...")

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
    in_input_prompt = False
    skipped_lines = 0
    for line in lines: 
        if '<div class="prompt input_prompt">' in line:
            # Don't write this line, or the next two lines.
            in_input_prompt = True
            skipped_lines = 1
            continue
        elif in_input_prompt:
            # Run this block exactly twice.
            skipped_lines += 1
            if skipped_lines > 3:
                # Write current line, and reset relevant flags.
                f.write(line.encode('utf-8'))
                in_input_prompt = False
                skipped_lines = 0
        else:
            # Regular line, write it.
            f.write(line.encode('utf-8'))
                
    f.close()


print("Stripped input reference numbers.\n")

