# multiprocessing
# 果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？
#
# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
#
# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束

# 子进程需要执行的代码

import os, time, random

from multiprocessing import Process


def run_proc(name):
    print('Run Child Process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent Process %s ' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child run')
    p.start()
    p.join()
    print('Child end')

# 运行结果
# Parent Process 2852
# Child run
# 15008
# Run Child Process aa (15008)
# Child end

print('===============================================================')
