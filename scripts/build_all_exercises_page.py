# This script scrapes all html pages, pulls out the exercises
#  and challenges, and copies them to the all_exercises_challenges.html
#  page.



import os
import sys

print("Building all_exercises_challenges.html...")

path_to_notebooks = '/srv/projects/intro_programming/intro_programming/notebooks/'

# Work through notebooks in the order listed here.
filenames = ['var_string_num.html']

# one file for testing:
#filenames = ['var_string_num.html']


# Grab all exercises and challenges:
html_string = ""
for filename in filenames:

    # Grab entire page
    f = open(path_to_notebooks + filename, 'r')
    lines = f.readlines()
    f.close()

    for index, line in enumerate(lines):
        # Probably need the line immediately before this!
        if '<h2 id="exercises' in line:
            print('line:', line)
            print('line before:', lines[index-1])
            # Capture starting from the line before,
            #   which opens the div for the exercises.
            html_string += lines[index-1]
            html_string += line

            # Keep adding to html_string, until matching div closed.


# Read in all_exercises_challenges.html
f = open(path_to_notebooks + 'all_exercises_challenges.html', 'r')
lines = f.readlines()
f.close()

# Write html to all_exercises_challenges.html
f = open(path_to_notebooks + 'all_exercises_challenges.html', 'wb')

# Want to start writing this after the second <div class=container>
#  Could be "container" or 'container'?
containers_found = 0    
for line in lines: 
    if 'div' in line and 'class=' in line and 'container' in line:
        containers_found += 1
        if containers_found == 2:
            f.write(html_string.encode('utf-8'))

        #new_line = line.replace(old_fb_url, new_fb_url)
        #f.write(new_line.encode('utf-8'))
    
    # Need to write each line back to the file.
    f.write(line.encode('utf-8'))

f.close()


print("Built all_exercises_challenges.html...")


