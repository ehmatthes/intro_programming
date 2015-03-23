# This script runs through all the html files in notebooks/, and 
#  modifies data-href url to current page.
# Prefer this to blank data-href so button shows up on local dev env.

import os
import sys

print("Modifying facebook urls...")

# Find all files to work with.
path_to_notebooks = '/srv/projects/intro_programming/intro_programming/notebooks/'
filenames = []
for filename in os.listdir(path_to_notebooks):
    if '.html' in filename and filename != 'index.html':
        filenames.append(filename)

# one file for testing:
#filenames = ['hello_world.html']

# Modify url on each page:
old_fb_url = 'data-href="http://introtopython.org"'
for filename in filenames:

    new_fb_url = 'data-href="http://introtopython.org/%s"' % filename

    f = open(path_to_notebooks + filename, 'r')
    lines = f.readlines()
    f.close()

    f = open(path_to_notebooks + filename, 'wb')
    for line in lines: 
       if old_fb_url in line:
            new_line = line.replace(old_fb_url, new_fb_url)
            f.write(new_line.encode('utf-8'))
       else:
            f.write(line.encode('utf-8'))
    f.close()


print("Modified facebook urls.\n")


