from jinja2 import Environment, FileSystemLoader

my_template_path = '/srv/projects/intro_programming/intro_programming/notebooks/my_templates'
ipython_template_path = '/srv/projects/intro_programming/venv/lib/python3.4/site-packages/IPython/nbconvert/templates/html'
my_loader = FileSystemLoader([my_template_path, ipython_template_path])
env = Environment(loader=my_loader)

index_template = my_loader.load(env, 'index.tpl')
print(index_template)
print(index_template.render())
