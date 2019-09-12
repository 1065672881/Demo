# 用Python来编写脚本简化日常的运维工作是Python的一个重要用途。在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，如ps，top，free等等。要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码。
#
# 在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。顾名思义，psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块

# 获取CPU信息
import psutil

print(psutil.cpu_count())  # CPU数量
print(psutil.cpu_count(logical=False))  # CPU物理核心
# 2说明是双核超线程, 4则是4核非超线程
# 统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times())

# 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
# for t in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))


# 获取内存信息
# 使用psutil获取物理内存和交换内存信息，分别使用
print(psutil.virtual_memory())
print(psutil.swap_memory())

# 获取磁盘信息
# 可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息
print(psutil.disk_partitions())  # 磁盘分区信息
# 磁盘使用情况
print(psutil.disk_usage('/'))
# 磁盘IO
print(psutil.disk_io_counters())

# 获取网络信息
# psutil可以获取网络接口和网络连接信息
print(psutil.net_io_counters())  # 获取网络读写字节／包的个数
print(psutil.net_if_addrs())  # 获取网络接口信息
print(psutil.net_if_stats())  # 获取网络接口状态
print(psutil.net_connections())  # 获取当前网络连接信息
