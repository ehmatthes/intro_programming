# This script scrapes all html pages, pulls out the exercises
#  and challenges, and copies them to the all_exercises_challenges.html
#  page.

import os, sys, re

print("Building all_exercises_challenges.html...")

path_to_notebooks = '/srv/projects/intro_programming/intro_programming/notebooks/'

# Work through notebooks in the order listed here.
filenames = ['var_string_num.html', 'lists_tuples.html',
             ]

# one file for testing:
#filenames = ['var_string_num.html']


def get_h1_label(line):
    # Pulls the label out of an h1 header line.
    #  This should be the label for what a set of exercises relates to.
    label_re = "(<h1.*>)(.*)(</h1)"
    p = re.compile(label_re)
    m = p.match(line)
    if m:
        return m.group(2)


# Grab all exercises and challenges:
html_string = ""
for filename in filenames:

    # Grab entire page
    f = open(path_to_notebooks + filename, 'r')
    lines = f.readlines()
    f.close()

    in_exercises = False
    num_open_divs = 0
    num_closed_divs = 0
    # Will need to keep track of section that the exercises are part of.
    current_h1_label = ''

    for index, line in enumerate(lines):
        if '<h1' in line:
            current_h1_label = get_h1_label(line)
            #print('current_h1_label:', current_h1_label)

        if '<h2 id="exercises' in line:
            #print(current_h1_line)
            # This is the signature of an exercise block.
            in_exercises = True

            # Capture the previous line, which opens the div for the exercises.
            #  Current line will be captured in "if in_exercises" block.
            html_string += lines[index-1]
            num_open_divs = 1

            #print('line before:', lines[index-1])
            #print('line:', line)

            # Add the most recent h1 label to this line.
            line = line.replace('Exercises', 'Exercises - %s' % current_h1_label)
            #print("line: ", line)

        if in_exercises:
            # Keep adding to html_string, until matching div closed.
            # 1 open div now, count new opens, count new closes, 
            # stop adding when opens == closes

            # Store the current line
            html_string += line

            # Check to see if this is the last line
            # Currently assumes only one div or closing div per line.
            if '<div' in line:
                num_open_divs += 1
            if '</div' in line:
                num_closed_divs += 1
            if num_open_divs == num_closed_divs:
                in_exercises = False
                num_open_divs = 0
                num_closed_divs = 0

#print("html_string: \n%s" % html_string)

# Read in all_exercises_challenges.html
f = open(path_to_notebooks + 'all_exercises_challenges.html', 'r')
lines = f.readlines()
f.close()

# Write html to all_exercises_challenges.html
f = open(path_to_notebooks + 'all_exercises_challenges.html', 'wb')

# Want to start writing this after <body>
for line in lines: 
    if '<body>' in line:
        # Write line, then html_string
        f.write(line.encode('utf-8'))
        f.write(html_string.encode('utf-8'))

    # Need to write each line back to the file.
    f.write(line.encode('utf-8'))

f.close()


print("Built all_exercises_challenges.html...")
