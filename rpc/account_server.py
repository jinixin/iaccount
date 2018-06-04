# coding=utf-8

from thrift.server.TServer import TThreadedServer
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol

from rpc.iaccount import AccountService
from model.account import Account


class AccountServiceHandler(object):
    def do_login(self, account):
        return Account.login(account.auth_id, account.password, account.type)

    def do_register(self, account):
        return Account.register(account.auth_id, account.password, account.type, account.permit)


def start_server():
    handler = AccountServiceHandler()
    processor = AccountService.Processor(handler)  # 绑定AccountService服务的处理器

    socket = TSocket.TServerSocket('127.0.0.1', 8801)  # 服务器非阻塞式socket

    transport = TTransport.TBufferedTransportFactory()  # 设置传输
    protocol = TBinaryProtocol.TBinaryProtocolFactory()  # 设置协议

    t = TThreadedServer(processor, socket, transport, protocol)  # 设置服务器
    t.serve()  # 启动服务


if __name__ == '__main__':
    start_server()
