# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/25 11:46:50

from http.server import BaseHTTPRequestHandler
import json

def getdata():    
    returndata = {
        "total": 111,
        "contributions": 222
    }
    return returndata
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = getdata()
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return