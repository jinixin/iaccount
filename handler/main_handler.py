# coding=utf-8

import json
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def arg(self, name, default=None):
        return self.get_argument(name, default=default)

    def get(self):
        self.write(json.dumps(self._get()))

    def post(self):
        self.write(json.dumps(self._post()))

    def _get(self):
        pass

    def _post(self):
        pass
