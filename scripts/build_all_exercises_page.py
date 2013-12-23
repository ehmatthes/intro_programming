# This script scrapes all html pages, pulls out the exercises
#  and challenges, and copies them to the all_exercises_challenges.html
#  page.

import os, sys, re

print("Building all_exercises_challenges.html...")

path_to_notebooks = '/srv/projects/intro_programming/intro_programming/notebooks/'

# Work through notebooks in the order listed here.
filenames = ['var_string_num.html', 'lists_tuples.html',
             'introducing_functions.html', 'if_statements.html',
             'while_input.html', 'terminal_apps.html',
             'dictionaries.html', 
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


def get_h1_link(filename, line):
    # Pulls the anchor link from the h1 line, and builds a link to
    #  the anchor on that page.
    link_re = """(.*)(<a name=['"])(.*)(['"].*)"""
    p = re.compile(link_re)
    m = p.match(line)
    if m:
        link = "http://introtopython.org/%s#%s" % (filename, m.group(3))
        return link


def get_new_notebook_header(filename, lines):
    # Pulls the page title from the notebook. It's in the first <h1>
    #  block in each notebook.
    for line in lines:
        if '<h1' in line:
            title_re = """(<h1.*>)(.*)(</h1)"""
            p = re.compile(title_re)
            m = p.match(line)
            if m:
                link = "http://introtopython.org/%s" % filename
                header_html = '<div class="text_cell_render border-box-sizing rendered_html">\n'
                header_html += "<h1><a href='%s'>%s</a></h1>\n" % (link, m.group(2))
                header_html += "</div>\n"
                return header_html


def add_intro():
    # Add an intro to html_string, before adding any exercises.
    intro_string  = '<div class="text_cell_render border-box-sizing rendered_html">\n'
    intro_string += '<h1>All Exercises and Challenges</h1>'
    intro_string += '<p>This page pulls together all of the exercises and challenges from throughout <a href="http://introtopython.org">introtopython.org</a>.</p>'
    intro_string += '<p>Each set of exercises has a link to the relevant section that explains what you need to know to complete those exercises. If you are struggling with an exercise, try reading through the linked material, and see if it helps you solve the exercise you are working on.</p>'
    intro_string += '<p>Exercises are short, specific tasks that ask you to apply a certain concept in a specific way. Challenges are longer, and they ask you to combine different ideas you have been working with. Challenges also ask you to be a little more creative in the programs you are starting to write.</p>'

    intro_string += '</div>'
    return intro_string


def rebuild_anchor_links(filename, line):
    # Looks for an anchor tag. If present, rebuilds link to link
    #  back to place on page being scraped.
    anchor_re = """.*(<a href=['"]#(.*))['"].*"""
    anchor_re = """.*<a href=['"](#.*)['"].*"""
    p = re.compile(anchor_re)
    m = p.match(line)
    if m:
        anchor_link = m.group(1)
        new_link = "http://introtopython.org/%s%s" % (filename, anchor_link)
        return line.replace(anchor_link, new_link)
    else:
        return line


# Grab all exercises and challenges.
#  Start building html string.
html_string = ""
# Add an intro.
html_string += add_intro()
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
    h1_label_linked = ''

    # Add a header for each notebook that has exercises.
    html_string += get_new_notebook_header(filename, lines)

    for index, line in enumerate(lines):
        # Anchor links need to be rebuilt.
        #  Inefficient, runs for every line. Could be moved to just
        #  before a line is being written to html_string, 
        #  but not significant.
        line = rebuild_anchor_links(filename, line)

        if '<h1' in line:
            current_h1_label = get_h1_label(line)
            current_h1_link = get_h1_link(filename, line)
            h1_label_linked = "<a href='%s'>%s</a>" % (current_h1_link, current_h1_label)

        if '<h2 id="exercises' in line:
            # This is the signature of an exercise block.
            in_exercises = True

            # Capture the previous line, which opens the div for the exercises.
            #  Current line will be captured in "if in_exercises" block.
            html_string += lines[index-1]
            num_open_divs = 1

            # Add the most recent h1 label to this line.
            line = line.replace('Exercises', 'Exercises - %s' % h1_label_linked)

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
