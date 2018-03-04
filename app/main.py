# -*- coding: utf-8 -*-
from flask import Flask
from flask import Flask, Blueprint
from flask_restful import Api
from flask_restful_swagger import swagger
from flask_cors import CORS
from app.resources.equipment import Equipments
from app.conf.config import MySQL_URI
from app.db import db


def create_app():
    """创建App"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = MySQL_URI # 定义URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 是否开启跟踪
    db.init_app(app)
    CORS(app)  # 跨域支持
    api_bp = Blueprint('api', __name__)
    api = swagger.docs(Api(api_bp), apiVersion='0.1', resourcePath='/', description='EMDP_API', api_spec_url='/swagger') # swagger支持
    bind_resources(api)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app

def bind_resources(api):
    """绑定对应资源"""
    api.add_resource(Equipments, '/equipments',endpoint='equipments')
    
