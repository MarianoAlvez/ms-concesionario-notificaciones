# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 10:58:27 2022

@author: User
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
    
   