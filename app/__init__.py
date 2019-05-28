#!/usr/bin/python3  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@software: PyCharm 
@file: __init__.py.py 
@time: 2019/5/27 17:51 
@describe: flask 各类配置连接初始化
"""
import sys
import os
from flask_login import LoginManager
from config import Config
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")
# template_folder 需指定模板位置，否则报错，博客未提及
app = Flask(__name__, template_folder='../templates', static_folder="", static_url_path="")
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
Session(app)
login = LoginManager(app)
login.login_view = 'login'
app.config.from_object(Config)
db = SQLAlchemy(app)
# 绑定app和数据库，以便进行操作
migrate = Migrate(app, db)
from app import routes
