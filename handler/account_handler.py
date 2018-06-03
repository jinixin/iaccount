# coding=utf-8

from handler.main_handler import MainHandler
from model import Account


class LoginHandler(MainHandler):
    def _get(self):
        auth_id = self.arg('auth')
        pwd = self.arg('password')
        owner = self.arg('type')

        if not all([auth_id, pwd, owner]):
            return {'ret': 0}

        ret = Account.login(auth_id, pwd, owner)

        return {'ret': int(ret)}

    _post = _get


class RegisterHandler(MainHandler):
    def _get(self):
        auth_id = self.arg('auth')
        pwd = self.arg('password')
        owner = self.arg('type')
        role = self.arg('permit')

        if not all([auth_id, pwd, owner]):
            return {'ret': 0}

        ret = Account.register(auth_id, pwd, owner, role)

        return {'ret': int(ret)}

    _post = _get
