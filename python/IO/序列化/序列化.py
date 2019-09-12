# 在程序运行的过程中，所有的变量都是在内存中
# 可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。
#
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
#
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
#
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
#
# Python提供了pickle模块来实现序列化。\
# 首先，我们尝试把一个对象序列化并写入文件

import pickle
import json

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象
f1 = open('dump.txt', 'rb')
d = pickle.load(f1)
f1.close()
# 当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
#
# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系


# JSON

# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON
# 首先导入import json
d1 = dict(name='Bob', age=20, score=88)
jsonStr = json.dumps(d1)
print("json : ", jsonStr)
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
#
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
print(json.loads(jsonStr))


# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换


# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化


class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student("MAX", 20, 88)


# print(json.dumps(s))


# 运行代码，毫不留情地得到一个TypeError
# 错误的原因是Student对象不是一个可序列化为JSON的对象
# 前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可


def stu_defalut_json(stu):
    return {
        'name': stu.name,
        'age': stu.age,
        'score': stu.score
    }


# 运行结果 : {"name": "MAX", "age": 20, "score": 88}
js = json.dumps(s, default=lambda obl: obl.__dict__)
print(js)


# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例


def dict_student(d):
    return Student(d['name'], d['age'], d['score'])


s1 = json.loads(js, object_hook=dict_student)
print(s1.name)
