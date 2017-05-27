"""Script to run conversion from ipynb to html."""

import os

from subprocess import run

print("Converting all ipynb files in notebooks/ to html.")
print("cwd:", os.getcwd())

# This should walk all dirs in notebooks/, find all ipynb files, then convert each.


# Need to run any pre-processing on raw .ipynb files?
#  ie, respond to any cell metadata or tags?
#  can remove cells that are tagged "invisible"

# This command is a little fragile. It needs to be modified to match how the user
#  runs python commands on their system.

run(["python3.6", "-m", "nbconvert", "notebooks/python_essentials/hello_world.ipynb", "--template=resources/my_templates/intro_python_base.tpl",
        "--FilesWriter.build_directory='html_site'"])

run(["python3.6", "-m", "nbconvert", "notebooks/python_essentials/var_string_num.ipynb", "--template=resources/my_templates/intro_python_base.tpl",
        "--FilesWriter.build_directory='html_site'"])

# run(["python3.6", "-m", "nbconvert", "notebooks/python_essentials/if_statements.ipynb", "--template=resources/my_templates/intro_python_base.tpl",
#         "--FilesWriter.build_directory='html_site'"])
