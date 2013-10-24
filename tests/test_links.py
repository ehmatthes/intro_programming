import requests
import re
import os

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

# Issues:
#  (high priority) Should run through all html files, not just the one specified.
#  Should check anchor tags.
#  Should check locally, rather than deployed.
#    Need to be serving files locally first.
#    Start a simple server from this test to do so.
#    Lower priority; if working deployed, should work locally.
#    Local is default behavior, flag for deployed?
#      Separate script for deployed?
#  Should have option to test deployed files.
#    Separate test, or flag for this test?
#  Make sure file name accurately reflects what's being tested.

# Start a server locally, in the notebooks directory.
root_dir = '/srv/projects/intro_programming/intro_programming/notebooks/'
#os.chdir(root_dir)
# This could be improved by making sure port 8000 available.
#os.system('python -m SimpleHTTPServer 8000 &')
#server_pid = os.system('echo $$')
#print("Starting server with pid: ", server_pid)

filename = 'index.html'
f = open(root_dir + filename, 'r')
lines = f.readlines()
f.close()


def get_links(line):
    # Returns a list of links contained in a line of code
    links = []
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
        for link in get_links(line):
            # Ignore anchor tags for now
            if 'html' in link:
                links_to_check.append(link)


# Report on progress as test runs, but store bad links for final report.
#  dict: {link: status_code}
bad_links = {}
print "links to check: ", links_to_check
for link in links_to_check:
    print "Checking link: %s..." % link
    #root = 'http://introtopython.org/'
    root = 'http://localhost:8000/'
    url = root + link
    print 'checking url: ', url
    r = requests.get(url)
    print 'Status code: ', r.status_code
    if r.status_code != 200:
        bad_links[link] = r.status_code


# Kill the server process
#kill_server_command = 'kill -9 ' + str(server_pid)
#os.system(kill_server_command)

# Report on bad links.
print "\n\n*** Bad Links ***"
if bad_links:
    for link in bad_links:
        print bad_links[link], link
else:
    print "Congratulations, all links are working."
print "\n"
