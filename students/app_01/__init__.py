from flask import Blueprint
# 配置蓝图
app_1 = Blueprint("app_1",__name__)
# 导入函数
from . import studentsystem

# studentsystem_01 没作用忽略
