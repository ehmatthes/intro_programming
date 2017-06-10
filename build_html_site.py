"""Script to run conversion from ipynb to html."""
# Find all ipynb files in notebooks/, then convert each.
#   It should also preserve the directory structure found in notebooks/

# If you just run a server from html_site, you'll need to restart it
#   every time you run this script because html_site gets rebuilt.
# For development work, run this command from root directory:
#     $ python build_html_site.py && cd html_site/ && python3.6 -m http.server && cd ..
#   Then each time you modify build_html_site.py, ctrl-c the running server process
#   and rerun the command.


import os, sys
import shutil
from distutils import dir_util
import re

from subprocess import run


print("Converting all ipynb files in notebooks/ to html.")
print("  cwd:", os.getcwd())

# Delete existing html_site.
print("\nDeleting current html_site directory...")
try:
    shutil.rmtree('html_site')
    print("  Deleted html_site.")
except FileNotFoundError:
    print("  No html_site directory found.")


# Need to recreate dir structure from notebooks/ to html_site/.
#   Walk notebooks/, note the dir structure, and keep track of ipynb files
#     for further processing.
#   Also build any needed dirs in html_site, and copy any non-.py resources
#     to html_site.

# dict structure: ipynb_files{filename:path}
print("\nBuilding html_site directories, and copying non-.py resources...")
ipynb_files  = {}
for root, dirs, files in os.walk("notebooks"):
    for file in files:
        if file.endswith('.ipynb') and '.ipynb_checkpoints' not in root:
            # Store ipynb file, and build directory if doesn't exist.
            ipynb_files[file] = root
            
            new_dir = root.replace('notebooks', 'html_site')
            os.makedirs(new_dir, exist_ok=True)

        # Look for resources/, keep if any non-.py files.
        current_dir = root.split('/')[-1]
        if current_dir == 'resources':
            # Check if any non-.py files in here.
            for root, dirs, files in os.walk(root):
                res_files = [file for file in files if not file.endswith('.py')]
                for res_file in res_files:
                    # Create directory if needed, and copy file to html_site.
                    src = os.path.join(root, res_file)
                    dst = root.replace('notebooks', 'html_site')
                    os.makedirs(dst, exist_ok=True)
                    shutil.copy2(src, dst)
print("  Built html_site directory, and copied non-.py resource files.")


# Copy js and css resources into html_site.
#  Note this is distutils.dir_util.copy_tree, not shutils.copytree.
#  The shutils version fails if parent directory exists.
print("\nCopying js and css resources into html_site...")
dir_util.copy_tree('resources/js', 'html_site/js')
dir_util.copy_tree('resources/css', 'html_site/css')
print("  Created html_site, and copied js and css resources.")


# Need to run any pre-processing on raw .ipynb files?
#  ie, respond to any cell metadata or tags?

# This gets the command used to run this script. If the user calls with python,
#  it uses that command, if they use python3.6, it uses that command.
python_caller = os.environ['_']

print("\nConverting all notebooks...")
for ipynb_file, path in ipynb_files.items():
    nb_filepath = os.path.join(path, ipynb_file)
    print("  converting:", nb_filepath)

    # For development purposes, it's often helpful to convert just one notebook.
    if 'var_string' not in nb_filepath:
        continue

    build_directory = path.replace('notebooks', 'html_site')

    # Calculate prefix for path to css and js, set as env var.
    os.environ['CSS_JS_PREFIX'] = build_directory.count('/') * '../'

    # This is manually determining which notebooks get show/hide all output buttons.
    #  Might be better to scrape the files, look for output cells, and only place
    #  show/hide all buttons on notebooks with output cells. Can this be done
    #  in the template?
    # DEV This should be replaced with a notebook metadata entry.
    if ipynb_file == 'index.ipynb':
        template = 'resources/my_templates/intro_python_index.tpl'
    else:
        template = 'resources/my_templates/intro_python_default.tpl'

    # This is using the command line version of nbconvert, because that's how I first
    #   learned to use it. But it's a bit awkward from here. Since we're in a Python
    #   script, it would be better to use nbconvert as a library. That might reduce need
    #   for separate files like scripts/my_config.py.
    # See: http://nbconvert.readthedocs.io/en/latest/nbconvert_library.html
    run([python_caller, "-m", "nbconvert", os.path.join(path, ipynb_file),
         "--config", "scripts/my_config.py",
         "--template={0}".format(template),
         "--FilesWriter.build_directory='{0}'".format(build_directory),
         "--to", "scripts.css_js_exporter.CssJsExporter",
         "--TemplateExporter.exclude_input_prompt=True",
         ])

