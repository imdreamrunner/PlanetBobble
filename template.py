import os
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Template:
    def __init__(self, filename):
        self.t = JINJA_ENVIRONMENT.get_template(filename)

    def render(self, *var):
        return self.t.render(var)