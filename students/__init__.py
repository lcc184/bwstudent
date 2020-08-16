from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 此处python3.8运行报错，执行此功能，不支持mysql，降低版本重新配置环境
# import pymysql
# pymysql.install_as_MySQLdb()
from config import Config
# 配置数据库
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)


    config_class = Config()
    # 实例化类
    app.config.from_object(config_class)
    # 初始化
    db.init_app(app)
    # 配置蓝图
    from students import app_01
    app.register_blueprint(app_01.app_1,url_prefix="/")

    return app