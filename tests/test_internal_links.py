import requests
import re

# This test runs through all html files in /notebooks,
#  and verifies that internal links are working.

# for html_file in html_files
#  for line in html_file
#   if <a href
#    request page locally
#     assert result 200
#      except log page, link, result
#      output ongoing
#      final report of error links

filename = '/srv/projects/intro_programming/intro_programming/notebooks/index.html'
f = open(filename, 'r')
lines = f.readlines()
f.close()

def get_links(line):
    # Returns a list of links contained in a line of code
    links = []
    link_re = '.*a href.*'
    link_re = '(.*a href=")(.*)(".*)'
    link_re = '=(")(.*)(".*)'
    p = re.compile(link_re)

    # Split lines so they start with links.
    #  ie, segments will be ~ ="hello_world.html">blah
    for segment in line.split('a href'):
        m = p.match(segment)
        if m:
            #print 'match: ', m.group(2)
            links.append(m.group(2))

    return links

# Store all links to check.
links_to_check = []
for line in lines:
    if 'a href' in line:
        #print line
        for link in get_links(line):
            # Ignore anchor tags for now
            if 'html' in link:
                links_to_check.append(link)

print 'Links:'
# Report on progress as test runs, but store bad links for final report.
#  dict: {link: status_code}
bad_links = {}
for link in links_to_check:
    print "Checking link: %s..." % link
    root = 'file:///srv/projects/intro_programming/intro_programming/notebooks/'
    root = 'http://introtopython.org/'
    r = requests.get(root + link)
    print 'Status code: ', r.status_code
    if r.status_code != 200:
        bad_links[link] = r.status_code

# Report on bad links.
print "\n\n*** Bad Links ***"
if bad_links:
    for link in bad_links:
        print bad_links[link], link
else:
    print "Congratulations, all links are working."
