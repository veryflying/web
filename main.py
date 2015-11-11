#coding=gbk
import web
import os
import word
import tb
import re


urls = (
    '/hello/(.*)', 'Hello',
    '/t/(.*)', 'Translate',
    '/', 'Index',
    '/tb/?.*', 'Taobao'
)

app = web.application(urls, globals())


class Taobao:
    def __init__(self):
        pass


    def GET(self):
        user_data = web.input()
        try:
            id_ = user_data.id
        except:
            id_ = ''
        if len(id_) == 0:
            templ = web.template.frender('history_tb.html')
            return templ(None)
        # if re.search(r'^\d+$', id_) is None:
        #     mthd = re.search(r'.*?id=(\d+).*', id_)
        #     if mthd is None:
        #         return 'URL错误'
        #     else:
        #         id_ = mthd.group(1)
        url = tb.short_url_tb(id_)
        result = tb.get_from_mmm(url)
        templ = web.template.frender('history_tb.html')
        # result['title'] = tb.get_title(url)
        return templ(result)


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


class Index:
    def __init__(self):
        pass


    def GET(self):
        index = web.template.frender('index.html')
        return index()


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    # sys.argv[1] = port
    app.run()