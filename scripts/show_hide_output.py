# This script runs through all the html files in notebooks/, and adds
#  in code to allow toggling of output.

import os
import re
import sys

# Find all files to work with.
path_to_notebooks = '/srv/projects/intro_programming/intro_programming/notebooks/'
filenames = []
for filename in os.listdir(path_to_notebooks):
    if '.html' in filename and filename != 'index.html':
        filenames.append(filename)

# Test with one simple file.
#filenames = ['hello_world.html']



def generate_button(id_number):
    # Generate the button code to place before each div.output
    button_string =  "<div class='text-right'>\n"
    button_string += "    <button id='show_output_%d' class='btn btn-success btn-xs show_output'>show output</button>\n" % id_number
    button_string += "    <button id='hide_output_%d' class='btn btn-success btn-xs hide_output'>hide output</button>\n" % id_number
    button_string += "</div>\n"
    return button_string


replacement_num = 0
# Find all div.output, and add an id to each.
for filename in filenames:

    f = open(path_to_notebooks + filename, 'r')
    lines = f.readlines()
    f.close()

    target_string = '<div class="output '
    f = open(path_to_notebooks + filename, 'wb')
    for line in lines:
        if target_string in line:
            # If this line has a div.output, add an id
            replacement_string = '<div id="output_%d" class="output ' % replacement_num
            
            # Add a pair of show/ hide buttons right before div.output
            f.write(generate_button(replacement_num))
            f.write(line.replace(target_string, replacement_string))
            replacement_num += 1
        else:
            # Otherwise, rewrite the line.
            f.write(line)












