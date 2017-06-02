"""Script to run conversion from ipynb to html."""
# Find all ipynb files in notebooks/, then convert each.
#  It should also preserve the directory structure found in notebooks/

import os, sys
import shutil
from distutils import dir_util
import re

from subprocess import run



print("Converting all ipynb files in notebooks/ to html.")
print("  cwd:", os.getcwd())

new_dirs = []
# dict structure: ipynb_files{filename:path}
ipynb_files  = {}
for root, dirs, files in os.walk("notebooks"):
    for file in files:
        if file.endswith('.ipynb') and '.ipynb_checkpoints' not in root:
            ipynb_files[file] = root
            
            new_dir = root.replace('notebooks', 'html_site')
            if new_dir not in new_dirs:
                new_dirs.append(new_dir)

# Delete existing html_site.
print("\nDeleting current html_site directory...")
try:
    shutil.rmtree('html_site')
    print("  Deleted html_site.")
except FileNotFoundError:
    print("  No html_site directory found.")

# Create any directory in html_site, including root, that doesn't already exist.
print("\nBuilding new html_site directory...")
for new_dir in new_dirs:
    os.makedirs(new_dir, exist_ok=True)
print("  Built html_site directory.")

# Copy js and css resources into html_site.
#  Note this is distutils.dir_util.copy_tree, not shutils.copytree.
#  The shutils version fails if parent directory exists.
print("\nCopying js and css resources into html_site...")
dir_util.copy_tree('resources/js', 'html_site/js')
dir_util.copy_tree('resources/css', 'html_site/css')
print("  Created html_site, and copied js and css resources.")


# Need to run any pre-processing on raw .ipynb files?
#  ie, respond to any cell metadata or tags?

# DEV: may need to copy images and some other resources, but not .py files.

# This gets the command used to run this script. If the user calls with python,
#  it uses that command, if they use python3.6, it uses that command.
python_caller = os.environ['_']

print("\nConverting all notebooks...")
for ipynb_file, path in ipynb_files.items():
    nb_filepath = os.path.join(path, ipynb_file)
    print("  converting:", nb_filepath)

    build_directory = path.replace('notebooks', 'html_site')

    # This is manually determining which notebooks get show/hide all output buttons.
    #  Might be better to scrape the files, look for output cells, and only place
    #  show/hide all buttons on notebooks with output cells. Can this be done
    #  in the template?
    if ipynb_file == 'index.ipynb':
        template = 'resources/my_templates/intro_python_index.tpl'
    else:
        template = 'resources/my_templates/intro_python_default.tpl'

    run([python_caller, "-m", "nbconvert", os.path.join(path, ipynb_file),
         "--template={0}".format(template),
         "--FilesWriter.build_directory='{0}'".format(build_directory),
         "--TemplateExporter.exclude_input_prompt=True",
         ])



# Post-processing of html files.
#   Some customization is not straightforward, or not possible through
#     nbconvert alone. For these steps, we work directly with the html files
#     in html_site/.
#   Ideally all of these steps will be replaced by more nuanced use of nbconvert
#     and templates.

# Modify css and js links to match directory level.
#   An html file in html_site/python_essentials/ needs to link to
#     ../css/site_styles.css, etc.
#   Find all html files in html_site, get nesting level from path structure,
#     and convert links appropriately.
#   This approach is almost identical to what's used above in finding
#     all ipynb files; may be appropriate to refactor this. Not necessary
#     if some or all of this can be done with nbconvert.

# Find all html files.
html_files  = {}
for root, dirs, files in os.walk("html_site"):
    for file in files:
        if file.endswith('.html'):
            html_files[file] = root

# Replace links in each file depending on length of path.
print("\nModifying links to css and js resources...")
for html_file, path in html_files.items():
    html_filepath = os.path.join(path, html_file)
    # Nesting level is number of steps in path, equivalent to
    #  number of slashes minus 1. html_site/ doesn't count.
    nesting_level = html_filepath.count('/') - 1
    prefix = '../' * nesting_level
    
    css_re = r'<link href="css'
    js_re = r'src="js/'
    # Open file, copy text, make substition, rewrite file.
    with open(html_filepath) as f:
        file_text = f.read()
    new_css_link = '<link href="{0}css'.format(prefix)
    new_js_link = 'src="{0}js/'.format(prefix)
    new_file_text = re.sub(css_re, new_css_link, file_text)
    new_file_text = re.sub(js_re, new_js_link, new_file_text)
    with open(html_filepath, 'w') as f:
        f.write(new_file_text)
