# datetime是Python处理日期和时间的标准库。
# 获取当前日期和时间
from datetime import datetime,timedelta, timezone
now = datetime.now()
print(now)

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 23, 59, 59)
print(dt)

# datetime转换为timestamp 日期转时间戳
# 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：
dts = datetime(2015, 4, 19, 23, 59, 59)
print(str(dts.timestamp()).split('.')[0])

# timestamp转换为datetime
# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
ts = 1429459199.0
print(datetime.fromtimestamp(ts))
# timestamp也可以直接被转换到UTC标准时区的时间：
print(datetime.utcfromtimestamp(ts))

# 字符转换为datetime
# 转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串
# 注意转换后的datetime是没有时区信息的
day = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(day)

# datetime转换为字符
now = datetime.now()
strNow = now.strftime('%Y-%m-%d %H:%S:%M')
print(isinstance(strNow, str))

# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类
now = datetime.now()
print(now)
now += timedelta(hours=10)
print(now)

# 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
# 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。
utc_time = timezone(timedelta(hours=8))
print(utc_time)
now = datetime.now()
dt = now.replace(tzinfo=utc_time)
print(dt)

# 时区转换
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
utc_now_time = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_now_time)
# astimezone()将转换时区为北京时间:
bj_time = utc_now_time.astimezone(timezone(timedelta(hours=8)))
print(bj_time)
# 区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
# 注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。
