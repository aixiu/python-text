# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/25 11:46:50

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask Github!'