# coding=utf-8

import hashlib

from base.mongo_base import db
from model.owner import Owner


class Account(object):
    collection = db['account']

    id = '_id'
    auth_id = 'ai'
    password = 'pd'
    role = 'rl'  # "0000 0000"八位二进制形式，拥有某项权力，则对应位为1
    owner = 'or'

    @classmethod
    def login(cls, auth_id, pwd, owner):
        target_pwd = hashlib.md5(bytes(pwd, 'utf-8')).hexdigest()
        owner = Owner.get(owner)
        if owner is None:
            return False

        doc = {
            cls.auth_id: auth_id,
            cls.password: target_pwd,
            cls.owner: owner,
        }
        ret = cls.collection.count(filter=doc)

        return True if ret else False

    @classmethod
    def register(cls, auth_id, pwd, owner, role=0):
        pwd_md5 = hashlib.md5(bytes(pwd, 'utf-8')).hexdigest()
        owner = Owner.get(owner)
        if owner is None or cls.has_register(auth_id, owner) is not False:
            return False

        doc = {
            cls.auth_id: auth_id,
            cls.password: pwd_md5,
            cls.role: role,
            cls.owner: owner,
        }
        ret = cls.collection.insert_one(document=doc)

        return True if ret else False

    @classmethod
    def has_register(cls, auth_id, owner):
        """ 返回值为三态, True已注册, False未注册, None所属工程不明 """
        if not isinstance(owner, int):
            owner = Owner.get(owner)

        if owner is None:
            return None

        d = {
            cls.auth_id: auth_id,
            cls.owner: owner,
        }
        ret = cls.collection.count(filter=d)

        return True if ret else False
