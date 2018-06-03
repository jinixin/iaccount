# coding=utf-8


class Owner(object):
    """ 标识某账号的所属工程, 从1000开始递增 """
    BERRY = 1000

    @classmethod
    def has(cls, owner):
        return hasattr(cls, str(owner))

    @classmethod
    def get(cls, owner):
        return getattr(cls, owner, None)


if __name__ == '__main__':
    print(Owner.has('BERRY'))
    print(Owner.get('BERRY'))
