"""Script to run conversion from ipynb to html."""
# Find all ipynb files in notebooks/, then convert each.
#  It should also preserve the directory structure found in notebooks/

# DEV:
#  Also need to copy resources such as images over to html_site?
#   But not .py files.

import os, sys

from subprocess import run


print("Converting all ipynb files in notebooks/ to html.")
print("cwd:", os.getcwd())

new_dirs = []
#pynb_files{path:filename}
ipynb_files  = {}
for root, dirs, files in os.walk("notebooks"):
    for file in files:
        if '.ipynb' in file:
            ipynb_files[root] = file
            
            new_dir = root.replace('notebooks', 'html_site')
            if new_dir not in new_dirs:
                new_dirs.append(new_dir)

# Create any directory in html_site, including root, that doesn't already exist.
#  Should this clear out js and css from html_site, and all other dirs?
for new_dir in new_dirs:
    os.makedirs(new_dir, exist_ok=True)

sys.exit()



# Need to run any pre-processing on raw .ipynb files?
#  ie, respond to any cell metadata or tags?
#  can remove cells that are tagged "invisible"

# This command is a little fragile. It needs to be modified to match how the user
#  runs python commands on their system. Could say python by default, but accept
#  a command line argument if the user has a different python command on their system.
#  For example, one of my machines uses the command python3.6 instead of python.
#  python for system python, python3.6 for latest version.

run(["python3.6", "-m", "nbconvert", "notebooks/python_essentials/hello_world.ipynb", "--template=resources/my_templates/intro_python_base.tpl",
        "--FilesWriter.build_directory='html_site'"])

run(["python3.6", "-m", "nbconvert", "notebooks/python_essentials/var_string_num.ipynb", "--template=resources/my_templates/intro_python_base.tpl",
        "--FilesWriter.build_directory='html_site'"])

# run(["python3.6", "-m", "nbconvert", "notebooks/python_essentials/if_statements.ipynb", "--template=resources/my_templates/intro_python_base.tpl",
#         "--FilesWriter.build_directory='html_site'"])
