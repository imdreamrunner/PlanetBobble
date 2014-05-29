import os

import webapp2
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class IndexHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'word': "Hello World!"
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', IndexHandler)
], debug=True)
