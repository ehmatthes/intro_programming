from jinja2 import Environment, FileSystemLoader

# Load index template.
my_template_path = '/srv/projects/intro_programming/intro_programming/notebooks/my_templates'
my_template_base_path = '/srv/projects/intro_programming/intro_programming/notebooks'
ipython_template_path = '/srv/projects/intro_programming/venv/lib/python3.4/site-packages/IPython/nbconvert/templates/html'

my_loader = FileSystemLoader(
    [my_template_path, my_template_base_path, ipython_template_path])
env = Environment(loader=my_loader)

index_template = my_loader.load(env, 'index.tpl')

# Render template to file.
notebooks_path = '/srv/projects/intro_programming/intro_programming/notebooks/'
filepath = notebooks_path + 'index.html'
with open(filepath, 'w') as f:
    f.write(index_template.render())
