"""Script to run conversion from ipynb to html."""

import os

from subprocess import run

print("Converting all ipynb files in notebooks/ to html.")
print("cwd:", os.getcwd())

run(["python", "-m", "nbconvert", "hello_world.ipynb", "--template=my_templates/intro_python_base.tpl"])

