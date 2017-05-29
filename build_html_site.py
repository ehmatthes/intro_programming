"""Script to run conversion from ipynb to html."""
# Find all ipynb files in notebooks/, then convert each.
#  It should also preserve the directory structure found in notebooks/

# DEV:
#  Also need to copy resources such as images over to html_site?
#   But not .py files.

import os, sys

from subprocess import run
from shutil import rmtree


print("Converting all ipynb files in notebooks/ to html.")
print("  cwd:", os.getcwd())

new_dirs = []
# dict structure: ipynb_files{path:filename}
ipynb_files  = {}
for root, dirs, files in os.walk("notebooks"):
    for file in files:
        if file.endswith('.ipynb'):
            ipynb_files[root] = file
            
            new_dir = root.replace('notebooks', 'html_site')
            if new_dir not in new_dirs:
                new_dirs.append(new_dir)

# Delete html_site, or empty it. Copy js and css resources to the directory.
print("\nDeleting current html_site directory...")
try:
    rmtree('html_site')
    print("  Deleted html_site.")
except FileNotFoundError:
    print("  No html_site directory found.")

# Create any directory in html_site, including root, that doesn't already exist.
print("\nBuilding new html_site directory...")
for new_dir in new_dirs:
    os.makedirs(new_dir, exist_ok=True)
print("  Built html_site directory.")

sys.exit()



# Need to run any pre-processing on raw .ipynb files?
#  ie, respond to any cell metadata or tags?
#  can remove cells that are tagged "invisible"

# This gets the command used to run this script. If the user calls with python,
#  it uses that command, if they use python3.6, it uses that command.
python_caller = os.environ['_']

run([python_caller, "-m", "nbconvert", "notebooks/python_essentials/hello_world.ipynb", "--template=resources/my_templates/intro_python_base.tpl",
        "--FilesWriter.build_directory='html_site'"])

run([python_caller, "-m", "nbconvert", "notebooks/python_essentials/var_string_num.ipynb", "--template=resources/my_templates/intro_python_base.tpl",
        "--FilesWriter.build_directory='html_site'"])

# run([python_caller, "-m", "nbconvert", "notebooks/python_essentials/if_statements.ipynb", "--template=resources/my_templates/intro_python_base.tpl",
#         "--FilesWriter.build_directory='html_site'"])
