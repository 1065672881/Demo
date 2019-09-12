import requests

# 要通过GET访问一个页面，只需要几行代码
r = requests.get('https://www.baidu.com/')
print(r.status_code)
print(r.text)

# 对于带参数的URL，传入一个dict作为params参数：
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.status_code)

# requests自动检测编码，可以使用encoding属性查看：
print(r.encoding)

# 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
print(r.content)

# requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：
# rs = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(rs.json())

# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
rp = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(rp.status_code)

# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
params = {
    'key': 'value0'
}
rs = requests.post('https://accounts.douban.com/login', json=params)
print(rs.status_code)

# 类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数

# 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
#
# 把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。

# upload_files = {'file': open('report.xls', 'rb')}

# r = requests.post(url, files=upload_files)

# 除了能轻松获取响应内容外，requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头
