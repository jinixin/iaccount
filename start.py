# coding=utf-8

import tornado.ioloop
import tornado.web

from handler import RegisterHandler, LoginHandler


def make_app():
    app = tornado.web.Application(
        handlers=[
            (r'/login', LoginHandler),
            (r'/register', RegisterHandler),
        ],
    )
    return app


def main():
    app = make_app()
    app.listen(8889)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
