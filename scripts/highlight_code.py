# This script runs through all the html files in notebooks/, and 
#  converts `###highlight=[1,2,10,11,12]` directives to style directives
#  for highlighting lines of code in code cells.

# To highlight lines of code in a cell, add a comment on the first
#  line of the cell, starting with three pound symbols, the word
#  'highlight', and an equals sign with no space. Then write a Python
#  list, with each line to be highlighted listed. The script only reads
#  comma-separated values, not grouped values. 

# yes: '###highlight=[1,2,7,8,9]'
# no:  '###highlight=[1,2,7-9]'

# You can turn line numbering on in the notebook, and just use the line
#  numbers that are displayed. The script adjusts for the first line 
#  being taken up by the ###highlight= comment. The script also removes
#  the ###highlight= comment from the html file, but does not remove
#  the highlighting directive from the notebook itself.

# The script adds the style directive
# <div class="highlighted_code_line">...current code html...</div>
# to the selected code lines.

# The script assumes all html files are not nested, in a directory called
#  'notebooks'.

# You will need to specificy path_to_notebooks.
# I'm happy to hear feedback, and accept improvements:
# https://github.com/ehmatthes/intro_programming
# ehmatthes@gmail.com, @ehmatthes


import os, sys
import ast

print("\nHighlighting code...")

# Find all files to work with.
#  Replace with your path.
path_to_notebooks = '/srv/projects/intro_programming/intro_programming/notebooks/'

filenames = []
for filename in os.listdir(path_to_notebooks):
    if '.html' in filename and filename != 'index.html':
        filenames.append(filename)

# Uncomment to use just one file for testing:
#filenames = ['visualization_earthquakes.html']


# Process each file.
for filename in filenames:

    # Grab the lines from this html file.
    f = open(path_to_notebooks + filename, 'r')
    lines = f.readlines()
    f.close()

    # Open the file for rewriting.
    f = open(path_to_notebooks + filename, 'wb')

    # Create an empty list for the lines that will need to be highlighted.
    highlight_lines = []
    # True when in a code block that has some highlighting left to be done.
    highlighting_active = False

    # Next line to highlight; starts at 0 in each code block.
    #  This takes into account the ###highlight= line, so you don't have
    #  to do a bunch of subtracting while composing notebooks.
    highlight_line = None

    for line in lines: 
        if '###highlight' in line:
            # Get lines to highlight, stored as a list.
            #  Lines are in a list, after the equals sign.
            try:
                highlight_lines = ast.literal_eval(line[line.index('highlight=')+10:line.index(']')+1])
            except:
                print("Problem finding lines to highlight in %s near line %d" % (filename, lines.index(line)))
            
            # We have some lines to highlight. Start tracking lines,
            #  and highlight appropriate lines.
            line_number = 0
            highlighting_active = True

        if highlighting_active:
            # We are in a code block, with some lines left to highlight.
            if line_number == 0:
                # We are on the ###highlight= line, and we don't need this entire line.
                #  We do need some of the line, which sets up the code block.
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
                    # Get next line to highlight.
                    highlight_line = highlight_lines.pop(0)-1
                except:
                    # No more lines to highlight in this code block.
                    highlight_line = None
                    highlighting_active = False
            else:
                # Write line of code as is.
                f.write(line.encode('utf-8'))
                line_number += 1
        else:
            # No highlighting left to do in this code block, or
            #  not in a code block with highlighting.
            #  Write line as is.
            f.write(line.encode('utf-8'))

    f.close()

print("  Highlighted code.\n")
