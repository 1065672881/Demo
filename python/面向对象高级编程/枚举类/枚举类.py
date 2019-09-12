# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义
# 常量就是不可变的变量
# 更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例


from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar'))

print(Month.Jan.name)
# value属性则是自动赋给成员的int常量，默认从1开始计数。
for name, member in Month.__members__.items():
    print(name, "=>", member, ',', member.value)

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类


@unique
class Week(Enum):
    Sun = 'aaa'
    Mon = 1
    Tue = 2


print(Week.Sun.value)
# 访问该枚举类有若干种方法
day = Week.Sun
print(day)
print(Week.Sun)
print(Week['Sun'])
# 可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量





