import requests
import re
import os, subprocess, signal, sys
from getopt import getopt
from time import sleep

# This test runs through all html files in /notebooks,
#  and verifies that links are working.

# to do
#  check anchor tags as well
#  accept flag to check deployed pages
#  should I be using beautifulsoup to parse html?

# Get command-line arguments
#  -r --root: The root directory that files are served from
#  (not yet implemented) -d --directory: The directory where files are stored locally
#  Should clarify that this test currently pulls links from local files,
#   but can test deployed version of files. That only makes sense
#   if deployed version matches current local version.
#  Should either pull links locally, and test locally, or
#   pull from deployed site, and test deployed site.

root = 'http://localhost:8000/'
opts, args = getopt(sys.argv[1:], "r:", ["root=",])
for opt, arg in opts:
    if opt in ('--root', '-r'):
        root = arg + '/'
print("Using root: ", root)


def get_links_in_line(line):
    # Returns a list of links contained in a line of code.
    links = []

    # Split lines so they start with links.
    #  ie, segments will be ~ ="hello_world.html">blah
    link_re = """=(["'])(.*?)(["'].*)"""
    p = re.compile(link_re)
    for segment in line.split('a href'):
        m = p.match(segment)
        if m:
            #print 'match: ', m.group(2)
            links.append(m.group(2))
    return links

def get_links_in_file(root_dir, filename):
    # Returns a list of all the links in a file.
    f = open(root_dir + filename, 'r')
    lines = f.readlines()
    f.close()

    links_to_check = []
    for line in lines:
        if 'a href' in line:
            for link in get_links_in_line(line):
                # Ignore anchor tags for now
                if 'html' in link:
                    links_to_check.append(link)
    return links_to_check

def check_links(filename, links, bad_links, links_tested):
    # Checks all links given, and adds bad links to bad_links.
    print("links to check: ", links)
    for link in links:
        print("Checking link: %s..." % link)

        # Only check links that haven't already been checked:
        if link in links_tested:
            continue
        
        # External links don't need our root.
        if 'http' in link:
            url = link
        else:
            url = root + link
        print('checking url: ', url)
        r = requests.get(url)
        print('Status code: ', r.status_code)
        if r.status_code != 200:
            bad_links[filename + '---' + link] = r.status_code
        else:
            links_tested.append(link)

# Location of html files
#  Assume all files in this directory, no nesting
root_dir = '/srv/projects/intro_programming/intro_programming/notebooks/'

# Get all html filenames in this directory.
#  Use os.walk if files end up nested.
filenames = []
for filename in os.listdir(root_dir):
    if 'html' in filename:
        filenames.append(filename)


# Start a server locally, in the notebooks directory.
print("Starting server...")
cmd = 'chdir /srv/projects/intro_programming/intro_programming/notebooks/ && '
cmd += 'python -m SimpleHTTPServer'
pro = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)

# Make sure server has a chance to start before making request.
print("SLEEPING...")
sleep(1)

# Report on progress as test runs, but store bad links for final report.
#  dict: {page---link: status_code}
bad_links = {}

# Only test each unique link once.
links_tested = []
num_links_checked = 0

# Check links in all files.
#filenames = ['var_string_num.html']
for filename in filenames:
    links_to_check = get_links_in_file(root_dir, filename)
    check_links(filename, links_to_check, bad_links, links_tested)
    num_links_checked += len(links_to_check)

# Kill the server process
os.killpg(pro.pid, signal.SIGTERM)

# Report on bad links.
print("\n\n*** Bad Links ***")
if bad_links:
    for link in bad_links:
        print('\n', bad_links[link], link)
else:
    print("Congratulations, all links are working.")
print("\n")

print("Checked %d links." % num_links_checked)
print("Tested %d unique links." % len(links_tested))
