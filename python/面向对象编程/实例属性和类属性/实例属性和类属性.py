# 给实例绑定属性和使用self或者实例变量
# 如何给类绑定属性


class Studnet():
    name = "MAX"
# 这个属性虽然归类所有，但类的所有实例都可以访问到
# 不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性
