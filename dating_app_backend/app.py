from flask import Flask
from flask_cors import CORS

from db import db
from router import app_blueprint
import configs
from models import User, Tag

# models 数据库模型，数据表格
# service 封装数据库操作，向router提供服务
# service.model 推荐模型
# router 路由，前端交互api

app = Flask(__name__)
CORS(app)  # 跨域
app.register_blueprint(app_blueprint[0])  # 路由信息注册
app.config.from_object(configs)  # 读入相关配置
db.app = app  # 数据库初始化相关
db.init_app(app)

# 主要用于测试
@app.before_first_request
def create_db():
    db.drop_all()
    db.create_all()
    user = User('123456', 'lukx', 'password')
    user.userid = '999'
    tag = Tag(1, 'student')
    db.session.add(user)
    db.session.add(tag)
    db.session.commit()
    # user.tags.append(tag)
    # db.session.commit()


if __name__ == '__main__':
    app.run()


