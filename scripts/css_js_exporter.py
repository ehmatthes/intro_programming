import os

from nbconvert.exporters import HTMLExporter


class CssJsExporter(HTMLExporter):

    """Grabs an environment variable, and makes it available in the template."""

    def from_notebook_node(self, nb, resources=None, **kw):
        self.environment.globals['css_js_prefix'] = os.environ['CSS_JS_PREFIX']
        return super().from_notebook_node(nb, resources, **kw)
