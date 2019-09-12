# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
#
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
from multiprocessing import Process, Queue

import os, time, random

# 写数据进程执行的代码


def write(q):
    print("执行写入数据...")
    for val in ['A', 'B', 'C']:
        q.put(val)
        time.sleep(random.random())


# 读数据进程执行的代码


def read(q):
    print("执行读取数据...")
    while True:
        val = q.get(True)
        print(val)


if __name__ == '__main__':
    # 父进程创建Queue, 并传递给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # pw进程启动
    pw.start()
    # pr进程启动
    pr.start()
    # 等待pw结束，再运行pr
    pw.join()
    # pr里的进程循环是死循环，需强制退出
    pr.terminate()
