#coding=gbk
import web
import os
import word

urls = (
    '/hello/(.*)', 'Hello',
    '/t/(.*)', 'Translate',
)

app = web.application(urls, globals())


class Hello:
    def __init__(self):
        pass


    def GET(self, name):
        if not name:
            name = 'World'
        web.setcookie('cookie', 2, 100, secure=True)
        cookies = web.cookies()
        print cookies
        hello = web.template.frender('hello.html')
        return hello(name)


class Translate:
    def __init__(self):
        pass


    def GET(self, name):
        if not name:
            name = 'a'
        result = word.get_interp(name)
        tmpl = web.template.frender('tmpl.html')
        return tmpl({'word': name,
                     'meaning': result})


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    # sys.argv[1] = port
    app.run()