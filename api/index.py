# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/25 11:46:50

import uvicorn
from fastapi import FastAPI, Response
from api.crawler import main as new
import json

app = FastAPI()

@app.get("/api")
def news(response: Response, index: int = 0, origin: str = 'zhihu', cache: str = 'null'):
    response.headers["Cache-Control"] = "max-age=86400, immutable, stale-while-revalidate"
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    response.headers["Access-Control-Allow-Origin"] = "*"
    if origin == "undefined":
        origin = "zhihu"
    data = new(index, origin)
    json_data = json.dumps(data, ensure_ascii=True, indent=4)
        
    return(json_data.encode())


if __name__ == "__main__":
    uvicorn.run("index:app", host="127.0.0.1", port=62, log_level="info")