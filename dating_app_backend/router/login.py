from flask import Blueprint

login_blueprint = Blueprint(
    'login',
    __name__,
    url_prefix='/login'
)


# 测试用
@login_blueprint.route('/', methods=['GET'])
def test():
    return 'test'


# 用户登录 TODO
@login_blueprint.route('/login', methods=['POST'])
def user_login():
    return 'login'


# 用户注册 TODO
@login_blueprint.route('/signup', methods=['POST'])
def user_signup():
    return 'signup'
