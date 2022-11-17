# 最后两行代码的作用是把const类注册到sys.modules这个全局字典中。
class _const:
    class ConstError(TypeError):
        pass

    def __init__(self):
        self.__setattr__('', '')

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" % name)
        self.__dict__[name] = value


import sys

sys.modules[__name__] = _const()
