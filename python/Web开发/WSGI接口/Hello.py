# 我们先编写hello.py，实现Web应用程序的WSGI处理函数：
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, Web</h1>']
