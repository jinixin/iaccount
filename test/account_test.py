# coding=utf-8

import unittest

from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol

from rpc.iaccount import AccountService
from rpc.iaccount.ttypes import AccountInfo


class get_client(object):
    def __init__(self):
        self.transport = None

    def __enter__(self):
        socket = TSocket.TSocket('127.0.0.1', 8801)  # 产生socket

        self.transport = TTransport.TBufferedTransport(socket)  # 原生socket效率差，加Buffer
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)  # 编码协议
        client = AccountService.Client(protocol)
        self.transport.open()  # 建立连接
        return client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.transport.close()  # 断开连接


class TestAccountRPC(unittest.TestCase):
    def startUp(self):
        pass

    def tearDown(self):
        pass

    def test_for_login(self):
        account = AccountInfo()
        account.auth_id = 'mk@monkey.com'
        account.password = 'monkey'
        account.type = 'BERRY'
        with get_client() as client:
            self.assertTrue(client.do_login(account))


if __name__ == '__main__':
    unittest.main()
