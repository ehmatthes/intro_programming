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
    highlight_lines = []
    highlighting_active = False
    # Next line to highlight:
    highlight_line = None
    for line in lines: 
        if '###highlight' in line:
            # Get lines to highlight, stored as a list.
            #  Lines are in a list, after the equals sign.
            highlight_lines = ast.literal_eval(line[line.index('highlight=')+10:line.index(']')+1])
            
            # We have some lines to highlight. Start tracking lines,
            #  and highlight appropriate lines.
            line_number = 0
            highlighting_active = True

        if highlighting_active:
            # We are in a code block, with some lines to highlight.
            if line_number == 0:
                # We are on the highlight line, and we don't need this entire line.
                # sample line: <div class="highlight"><pre><span class="c">###highlight=[2,3]</span>
                # becomes: <div class="highlight"><pre>
                # keep until start of '<span'
                span_index = line.index('<span')
                f.write(line[:span_index].encode('utf-8'))
                line_number += 1
                # Next line to highlight:
                #  Minus 1 accounts for initial comment line ###highlight=...,
                #  which will be removed.
                highlight_line = highlight_lines.pop(0)-1
            elif line_number == highlight_line:
                # Change style so line is highlighted.
                line = "<div class='highlighted_code_line'>%s</div>" % line
                f.write(line.encode('utf-8'))
                line_number += 1
                try:
                    highlight_line = highlight_lines.pop(0)-1
                except:
                    highlight_line = None
                    highlighting_active = False
            else:
                # Write line of code as is.
                f.write(line.encode('utf-8'))
                line_number += 1
        else:
            # Not in a code block that has highlighting,
            #  write line as is.
            f.write(line.encode('utf-8'))

    f.close()

print("Highlighted code.\n")
