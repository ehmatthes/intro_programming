# This script runs through all the html files in notebooks/, and adds in 
#  bootstrap tags where appropriate.

import os
import subprocess
import sys

# Pull out navbar from custom index.html page
f = open('/srv/projects/intro_programming/intro_programming/ignored_resources/index.html', 'r')
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

#print navbar_string

final_js_string = """
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="js/jquery.js"></script>
    <script src="js/bootstrap.min.js"></script>
"""


# Find all files to work with.
path_to_notebooks = '/srv/projects/intro_programming/intro_programming/notebooks/'
filenames = []
for filename in os.listdir(path_to_notebooks):
    if '.html' in filename:
        filenames.append(filename)




# Insert navbar into each file, right after opening body tag.
#  How deal with newlines in this???
filename = '/srv/projects/intro_programming/intro_programming/notebooks/hello_world.html'
cmd = "sed -i s/%s/%s%s/ %s" % ('<body>', '<body>\n', navbar_string, filename)
#print cmd

f = open(filename, 'r')
lines = f.readlines()
f.close()

f = open(filename, 'wb')
for line in lines: 
   if '<body>' in line:
        f.write(line)
        f.write(navbar_string)
        f.write("\n\n\n\n")
        #print "--- WRITING NAVBAR LINE ---"
   elif '</body>' in line:
       f.write(final_js_string)
       f.write(line)
       #print "--- WRITING FINAL JS STRING ---"
   else:
        f.write(line)
        #print "writing hello line..."

f.close()




sys.exit()












filename = 'hello_world.html'

f = open(path_to_notebooks + filename, 'r')
lines = f.readlines()
f.close()

f = open(path_to_notebooks, 'wb')



