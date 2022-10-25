# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/25 11:46:50


from http.server import BaseHTTPRequestHandler
import json


def getdata(name):
    data = {'名字': name}
    return data

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        user = path.split('?')[1]
        data = getdata(user)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return