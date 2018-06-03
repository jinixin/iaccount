# coding=utf-8

import unittest

from model import Account


class TestUser(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_for_register(self):
        ret = Account.register('mk@monkey.com', 'monkey', 'BERRY')
        self.assertTrue(ret)

    def test_for_login(self):
        self.assertTrue(Account.login('mk@monkey.com', 'monkey', 'BERRY'))
        self.assertFalse(Account.login('mk@monkey.com', 'love', 'BERRY'))


if __name__ == '__main__':
    unittest.main()
