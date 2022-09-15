"""
main.py
后端的入口文件
"""
from flask import Flask


app = Flask(__name__)

if __name__ == '__main__':
    app.run()
