from flask_sqlalchemy import SQLAlchemy
from Server import app

db = SQLAlchemy()


class Config(object):
    # SQLALchemy的配置参数，Python3中需要使用pymysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:170596@43.143.147.21:3306/DatingAppDB'
    # 数据跟踪，数据库中的表格式修改后，模型类会跟着自动修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)
# 创建数据库SQLAlchemy的工具对象
db = SQLAlchemy(app)


# 创建数据库模型类
class User(db.Model):
    __tablename__ = 'tb_users'  # 指定表名
    id = db.Column(db.Integer, primary_key=True)  # 整型的主键，默认会自动增长
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128), unique=True)

    # role_id = db.Column(db.Integer, db.ForeignKey('tbl_roles.id'))  # 设置外键

    # 定义显示信息，定义之后，查询时显示对象的时候更直观
    def __repr__(self):
        return 'User object: name=%s'.format(self.name)

def init_db():
    with app.app_context():
        db.drop_all()  # 清除数据库中的所有数据
        db.create_all()  # 创建所有的表

def add_user(users:list)->None:
    for i in users:
        if type(i) != User:
            raise TypeError('The type of user in list is wrong.')
    db.session.add_all(users)
    db.session.commit()


init_db()
add_user(['1'])