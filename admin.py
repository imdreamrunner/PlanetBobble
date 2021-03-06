import json
import webapp2

from template import Template


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'word': "Hello World!"
        }
        t = Template("admin/login.html")
        self.response.write(t.render(template_values))


class PicListHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(Template('admin/pic.list.html').render())


class PicCreateHandler(webapp2.RedirectHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        obj = {
            'success': 'some var',
            'payload': 'some var',
        }
        self.response.out.write(json.dumps(obj))

routes = [
    ('/admin/login', LoginHandler),
    ('/admin/pic/list', PicListHandler),
    ('/admin/pic/create', PicCreateHandler)
]