import webapp2
import template


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'word': "Hello World!"
        }
        t = template.get("admin/login.html")
        self.response.write(t.render(template_values))


routes = [
    ('/admin/login', LoginHandler)
]