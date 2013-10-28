# This script runs through all the html files in notebooks/, and adds in 
#  bootstrap tags where appropriate.

import os
import subprocess


# Find all files to work with.
path_to_notebooks = '/srv/projects/intro_programming/intro_programming/notebooks/'
filenames = []
for filename in os.listdir(path_to_notebooks):
    if '.html' in filename:
        filenames.append(filename)

filename = 'hello_world.html'

f = open(path_to_notebooks + filename, 'r')
lines = f.readlines()
f.close()

f = open(path_to_notebooks, 'wb')



