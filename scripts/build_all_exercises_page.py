# This script scrapes all html pages, pulls out the exercises
#  and challenges, and copies them to the all_exercises_challenges.html
#  page.

import os, sys, re

print("\nBuilding all_exercises_challenges.html...")

path_to_notebooks = '/srv/projects/intro_programming/intro_programming/notebooks/'

# Work through notebooks in the order listed here.
filenames = ['var_string_num.html', 'lists_tuples.html',
             'introducing_functions.html', 'if_statements.html',
             'while_input.html', 'terminal_apps.html',
             'dictionaries.html', 'more_functions.html',
             'classes.html',
             ]

# one file for testing:
#filenames = ['var_string_num.html']


def add_contents(html_string):
    # Once all pages have been scraped, parse html_string and 
    #  build contents.
    toc_string = '<div class="text_cell_render border-box-sizing rendered_html">\n'
    toc_string += "<h1>Contents</h1>\n"

    new_html_string = ''
    section_num = 0
    ex_ch_num = 0
    for line in html_string.split("\n"):
        if '<h1>' in line:

            # Rewrite the html_string line to have id that I want.
            #  Pull out section title from line.
            section_anchor = '<a name="section_%d"></a>' % section_num
            new_line = line.replace('<h1>', '<h1>%s' % section_anchor)
            new_html_string += new_line + "\n"

            section_re = """(<h1.*>)(.*)(</a></h1>)"""
            p = re.compile(section_re)
            m = p.match(line)
            if m:
                toc_string += '<h2><a href="#section_%d">%s</a></h2>\n' % (section_num, m.group(2))

            section_num += 1

        elif ('id="exercises' in line 
            or 'id="challenges' in line
            or 'id="overall-exercises' in line
            or 'id="overall-challenges' in line):

            # Rewrite the html_string line to have id that I want.
            #  Pull out page title from line.
            ex_ch_anchor = '<a name="ex_ch_%d"></a>' % ex_ch_num
            new_line = re.sub(r"""<a name=['"].*?['"]></a>""", ex_ch_anchor, line)
            new_html_string += new_line + "\n"

            ex_ch_re = """<.*/a>(.*)<a href.*>(.*)</a>"""
            p = re.compile(ex_ch_re)
            m = p.match(line)
            if m:
                toc_string += '<h3 class="contents_level_two">%s<a href="#ex_ch_%d">%s</a></h3>\n' % (m.group(1), ex_ch_num, m.group(2))

            ex_ch_num += 1

        else:
            new_html_string += line + "\n"

    toc_string += "</div>\n"
    toc_string += "<hr />\n\n"

    return toc_string + new_html_string


def anchor_exercises(html_string):
    # Add an anchor link to each exercise, so people can share any
    #  individual exercise.
    # Use name of exercise as anchor, but watch for repeated names.
    #  If repeated name, add a number to anchor.
    anchors = []
    new_html_string = ''
    for line in html_string.split("\n"):
        ex_ch_re = """<h4 id="(.*?)">(.*?)</h4>"""
        p = re.compile(ex_ch_re)
        m = p.match(line)
        if m:
            anchor = m.group(1)
            name = m.group(2)
            if anchor in anchors:
                new_anchor = anchor
                append_num = 1
                while new_anchor in anchors:
                    new_anchor = anchor + '_%d' % append_num
                    append_num += 1
                anchor = new_anchor

            # Rewrite line to include anchor tag, and to link to this
            #  anchor tag.
            anchor_tag = '<a name="%s"></a>' % anchor
            new_line = '%s<h4 id="%s"><a href="all_exercises_challenges.html#%s">%s</a></h4>\n' % (anchor_tag, anchor, anchor, name)
            new_html_string += new_line
        else:
            new_html_string += line + "\n"

    return new_html_string


def add_intro(html_string):
    # Add an intro to html_string, before adding any exercises.
    intro_string  = '<div class="text_cell_render border-box-sizing rendered_html">\n'
    intro_string += '<h1>All Exercises and Challenges</h1>\n'
    intro_string += '<p>This page pulls together all of the exercises and challenges from throughout <a href="http://introtopython.org">introtopython.org</a>.</p>\n'
    intro_string += '<p>Each set of exercises has a link to the relevant section that explains what you need to know to complete those exercises. If you are struggling with an exercise, try reading through the linked material, and see if it helps you solve the exercise you are working on.</p>\n'
    intro_string += '<p>Exercises are short, specific tasks that ask you to apply a certain concept in a specific way. Challenges are longer, and they ask you to combine different ideas you have been working with. Challenges also ask you to be a little more creative in the programs you are starting to write.</p>\n'

    intro_string += '</div>\n'
    intro_string += '<hr />\n'
    return intro_string + html_string


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
        link = "%s#%s" % (filename, m.group(3))
        return link


def get_page_title(filename):
    # Pulls the page title from the notebook. It's in the first <h1>
    #  block in each notebook.
    for line in lines:
        if '<h1' in line:
            title_re = """(<h1.*>)(.*)(</h1)"""
            p = re.compile(title_re)
            m = p.match(line)
            if m:
                return m.group(2)


def get_new_notebook_header(filename, lines):
    # Creates an html string for a header for each notebook
    #  being scraped.
    page_title = get_page_title(filename)
    link = "%s" % filename
    header_html = '<div class="text_cell_render border-box-sizing rendered_html">\n'
    header_html += "<h1><a href='%s'>%s</a></h1>\n" % (link, page_title)
    header_html += "</div>\n"
    return header_html


def rebuild_anchor_links(filename, line):
    # Looks for an anchor tag. If present, rebuilds link to link
    #  back to place on page being scraped.
    anchor_re = """.*(<a href=['"]#(.*))['"].*"""
    anchor_re = """.*<a href=['"](#.*)['"].*"""
    p = re.compile(anchor_re)
    m = p.match(line)
    if m:
        anchor_link = m.group(1)
        new_link = "%s%s" % (filename, anchor_link)
        return line.replace(anchor_link, new_link)
    else:
        return line

def top_html():
    # Returns html for a link to top of page.
    top_string = '<div class="text_cell_render border-box-sizing rendered_html">\n'
    top_string += '<p><a href="#">top</a></p>\n'
    top_string += '</div>\n'
    top_string += '<hr />\n'
    return top_string

# Grab all exercises and challenges.
#  Start building html string.
html_string = ""
for filename in filenames:

    # Grab entire page
    f = open(path_to_notebooks + filename, 'r')
    lines = f.readlines()
    f.close()

    in_exercises_challenges = False
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

            # If this is Overall Exercises or Overall Challenges,
            #  link to the notebook not the last h1 section.
            # Naming inconsistency; still calling these pieces ...h1...
            if 'verall' in line:
                current_h1_link = "%s" % filename
                current_h1_label = get_page_title(filename)
                h1_label_linked = "<a href='%s'>%s</a>" % (current_h1_link, current_h1_label)


        if ('<h2 id="exercises' in line 
            or '<h2 id="challenges' in line
            or '<h1 id="overall-challenges' in line
            or '<h1 id="overall-exercises' in line):
            # This is the signature of an exercise block.

            # Capture the previous line, which opens the div for the exercises.
            #  Current line will be captured in "if in_exercises" block.
            # Only do this if in_exercises_challenges currently False.
            if not in_exercises_challenges:
                html_string += lines[index-1]

            in_exercises_challenges = True
            html_string += "\n"

            # Add the most recent h1 label to this line.
            if 'Exercises' in line:
                line = line.replace('Exercises', 'Exercises - %s' % h1_label_linked)
            elif 'Challenges' in line:
                line = line.replace('Challenges', 'Challenges - %s' % h1_label_linked)

            # Make sure these elements are all written at the h2 level:
            line = line.replace('h1', 'h2')

        if in_exercises_challenges:
            # Stop adding lines when reach next 'top'.
            #  Remove div that was opened for the top line.
            #  This approach allows multiple cells to be part of
            #   exercises and challenges, but still be scraped.
            if '<div class="text_cell_render border-box-sizing rendered_html">' in line:
                # If next line has a link to top, stop here.
                if '<a href="#">top</a>' in lines[index+1]:
                    in_exercises_challenges = False
                    html_string += "\n"
                    continue

            # Store the current line
            html_string += line

    # Finished scraping a notebook, add a link to top of this page.
    html_string += top_html()

# Pages have been scraped; build contents from html_string.
html_string = add_contents(html_string)
# Add an intro.
html_string = add_intro(html_string)
# Add anchor links to each exercise.
html_string = anchor_exercises(html_string)

# Read in all_exercises_challenges.html
f = open(path_to_notebooks + 'all_exercises_challenges.html', 'r')
lines = f.readlines()
f.close()


# DEV
# Write headers.
header_lines = ''
with open(path_to_notebooks + 'my_templates/intro_python_header.html') as f:
    header_lines = f.read()

# Write string as it is.
# DEV: This should be done with Jinja templates.
#  Yes! Writing from template writes template tags to the screen.
with open(path_to_notebooks + 'all_exercises_challenges.html', 'wb') as f:
    f.write(header_lines.encode('utf-8'))
    f.write(html_string.encode('utf-8'))
print("  Built all_exercises_challenges.html.")


sys.exit()

# Write html to all_exercises_challenges.html
f = open(path_to_notebooks + 'all_exercises_challenges.html', 'wb')

# Want to start writing this after <body>
for line in lines: 
    if '<body>' in line:
        # Write line, then html_string
        f.write(line.encode('utf-8'))
        f.write(html_string.encode('utf-8'))
        # Don't write this line twice.
        continue
    # Need to write each line back to the file.
    f.write(line.encode('utf-8'))

f.close()


print("  Built all_exercises_challenges.html.")
