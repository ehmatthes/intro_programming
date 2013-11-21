# This script runs through all the html files in notebooks/, and adds in 
#  bootstrap tags where appropriate.

import os
import subprocess
import sys

# Pull out navbar from custom index.html page
f = open('/srv/projects/intro_programming/intro_programming/html_resources/index.html', 'r')
lines = f.readlines()
f.close()

navbar_string = ''
in_navbar = False
num_open_divs = 0
num_closed_divs = 0
for line in lines:
    # Navbar is in first div for now, so at first div set True.
    #  Could start from 'Fixed navbar'
    if '<div' in line:
        in_navbar = True
        num_open_divs += 1

    if '</div' in line:
        num_closed_divs += 1

    if in_navbar:
        navbar_string += line

    if num_open_divs > 0 and num_open_divs == num_closed_divs:
        in_navbar = False
        break

# jquery is included in the header of each page, so I can use it elsewhere
#  ie for toggling output and exercises.
#    <script src="js/jquery.js"></script>
final_js_string = """
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="js/bootstrap.min.js"></script>
"""


# Find all files to work with.
path_to_notebooks = '/srv/projects/intro_programming/intro_programming/notebooks/'
filenames = []
for filename in os.listdir(path_to_notebooks):
    if '.html' in filename and filename != 'index.html':
        filenames.append(filename)

# Insert navbar into each file, right after opening body tag.
#  Then insert required js library at end of file.
for filename in filenames:

    f = open(path_to_notebooks + filename, 'r')
    lines = f.readlines()
    f.close()

    f = open(path_to_notebooks + filename, 'wb')
    for line in lines: 
       if '<body>' in line:
            f.write(line.encode('utf-8'))
            f.write(navbar_string.encode('utf-8'))
            f.write("\n\n".encode('utf-8'))
       elif '</body>' in line:
           f.write(final_js_string.encode('utf-8'))
           f.write(line.encode('utf-8'))
       else:
            f.write(line.encode('utf-8'))
    f.close()
