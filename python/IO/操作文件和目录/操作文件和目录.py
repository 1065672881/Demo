import os

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.name)
# 要获取详细的系统信息，可以调用uname()函数
# windows系统下uname不可用
# print(os.uname())

# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
print(os.environ)

# 要获取某个环境变量的值，可以调用os.environ.get('key')
print(os.environ.get('PATH'))

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
# os.path.join('/PythonProject/Demo/python/IO', 'dir')
# 然后创建一个目录:
# 注意，如果文件已存在将抛出错误信息
# 使用. 将在当前目录创建
# os.mkdir('.dirs')
# # 删掉一个目录:
# os.rmdir('.dirs')
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串 而Windows下会返回这样的字符串
os.path.join('Demo')
os.path.join('/dirs')
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('/path/demo/file.txt'))
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便
print(os.path.splitext('/path/demo/file.txt'))
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。


# 文件操作使用下面的函数。假定当前目录下有一个test.txt文件
# os.rename('test', 'test.py')
# os.remove('test.py')

# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
#
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
#
# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录

key = os.path.abspath('.')
for x in os.listdir(key):
    # size = os.path.getsize(x)
    # flag = '/' if os.path.isdir(x) else ''
    # print(size, flag)
    print(x)



