# 了解了WSGI框架，我们发现：其实一个Web App，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应。
#
# 但是如何处理HTTP请求不是问题，问题是如何处理100个不同的URL。
#
# 每一个URL可以对应GET和POST请求，当然还有PUT、DELETE等请求，但是我们通常只考虑最常见的GET和POST请求。
#
# 一个最简单的想法是从environ变量里取出HTTP请求的信息，然后逐个判断


# def application(environ, start_response):
#     method = environ['REQUEST_METHOD']
#     path = environ['PATH_INFO']
#     if method=='GET' and path=='/':
#         return handle_home(environ, start_response)
#     if method=='POST' and path='/signin':
#         return handle_signin(environ, start_response)

# 只是这么写下去代码是肯定没法维护了。
#
# 代码这么写没法维护的原因是因为WSGI提供的接口虽然比HTTP接口高级了不少，但和Web App的处理逻辑比，还是比较低级，我们需要在WSGI接口之上能进一步抽象，让我们专注于用一个函数处理一个URL，至于URL到函数的映射，就交给Web框架来做。
#
# 由于用Python开发一个Web框架十分容易，所以Python有上百个开源的Web框架。这里我们先不讨论各种Web框架的优缺点，直接选择一个比较流行的Web框架——Flask来使用。
#
# 用Flask编写Web App比WSGI接口简单（这不是废话么，要是比WSGI还复杂，用框架干嘛？），我们先用pip安装Flask
