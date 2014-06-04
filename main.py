import webapp2

from template import Template


class IndexHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'word': "Hello World!"
        }
        t = Template('index.html')
        self.response.write(t.render(template_values))


routes = [
    ('/', IndexHandler)
]

import admin

routes += admin.routes

app = webapp2.WSGIApplication(routes, debug=True)
