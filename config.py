# 配置数据库配置信息
class Config:
    SECRET_KEY = "lcc"
    SQLALCHEMY_DATABASE_URI = "mysql://root:123@127.0.0.1:3306/students_1905c"  # 数据库连接URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 当数据库中数据发生变化后会自动同步到数据库模型类的属性中
