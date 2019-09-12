# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
#
# 来看看多个线程同时操作一个变量怎么把内容给改乱了

import time,threading

balance = 0


def change_it(n):
    # 声明为全局变量
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# 我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，但是，由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。

# 原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算
# balance = balance + n
# 也会分为两步
# 1. 计算banlance + n，并存入临时变量
# 2. 将临时变量的值给balance
# 也就是可以看成
# x = balance + n
# balance = x
# 由于x是局部变量，两个线程各自都有自己的x，当代码正常执行时
balance = 0
x1 = balance + 5
balance = x1
x1 = balance - 5
balance = x1

x2 = balance + 8
balance = x2
x2 = balance - 8
balance = x2
# 执行结果是0

# 但两个线程是交替执行,如下
balance = 0
x1 = balance + 5
x2 = balance + 8
balance = x2
balance = x1
x1 = balance - 5
balance = x1
x2 = balance - 8
balance = x2
# 此时结果是 -8
# 究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。
#
# 两个线程同时一存一取，就可能导致余额不对，你肯定不希望你的银行存款莫名其妙地变成了负数，所以，我们必须确保一个线程在修改balance的时候，别的线程一定不能改
# 如果确保多个线程执行正确，需要给线程上一把锁,当某个线程开始执行，可以说因为这个线程获取了锁，其他线程需等待此线程释放该锁，然后后续线程获取锁再开始执行,无论如何，同一时刻多个线程只有一个线程持有锁的权限
# 创建一个锁就是通过threading.Lock()来实现
money = 0
lock = threading.Lock()


def change_it_new(n):
    # 声明为全局变量
    global balance
    balance = balance + n
    balance = balance - n


def run_lock_thread(n):
    for i in range(100000):
        # 获取锁
        lock.acquire()
        try:
            change_it_new(n)
        finally:
            # 释放锁
            lock.release()


c1 = threading.Thread(target=run_lock_thread, args=(5,))
c2 = threading.Thread(target=run_lock_thread, args=(8,))
c1.start()
c2.start()
c1.join()
c2.join()
print(money)
