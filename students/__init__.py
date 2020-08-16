from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import pymysql
# pymysql.install_as_MySQLdb()
from config import Config
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)


    config_class = Config()
    app.config.from_object(config_class)
    db.init_app(app)
    from students import app_01
    app.register_blueprint(app_01.app_1,url_prefix="/")

    return app