""" Simple ORM using metaclass """

# 首先来定义Field类，它负责保存数据库表的字段名和字段类型


class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s : %s>' % (self.__class__.__name__, self.name)

# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

# 下一步，就是编写最复杂的ModelMetaclass了


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found Model : %s' % name)
        mappings = dict()
        for key, val in attrs.items():
            if isinstance(val, Field):
                print('Found Mapping : %s ==> %s' % (key, val))
                mappings[key] = val
            for k in mappings.keys():
                attrs.pop(k)
            attrs['__mapping__'] = mappings
            attrs['__table__'] = name
            return type.__new__(cls, name, bases, attrs)

# 以及基类Model：


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        field = []
        params = []
        args = []
        for k, v in self.mappings.items():
            field.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s values(%s)' & (self.__table__, ','.join(field), ','.join(params))
        print("SQL: %s" % sql)
        print("ARGS: %s" % str(args))

# 定义用户类


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    emial = StringField('email')
    password = StringField('password')


u = User(id=123456, name='MAX', email='123456@163.com', password='system')
u.save()
