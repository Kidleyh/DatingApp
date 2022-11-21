from flask import Blueprint, request, jsonify, json
from service.login_service import check_phone_exist, check_username_exist, check_password
from service.user_service import create_user, find_user_by_phone

login_blueprint = Blueprint(
    'login',
    __name__,
    url_prefix='/login'
)


# 测试用
@login_blueprint.route('/', methods=['GET'])
def test():
    return 'test'


@login_blueprint.route('/login', methods=['POST'])
def user_login():
    data = json.loads(request.get_data(as_text=True))
    phone = data['phoneNum']
    password = data['password']

    if not check_phone_exist(phone):
        return jsonify({'code': 401, 'msg': '登录失败', 'data': ''})  # phone doesn't exist
    if not check_password(phone, password):
        return jsonify({'code': 401, 'msg': '登录失败', 'data': ''})  # password doesn't fit

    user = find_user_by_phone(phone)
    res_data = dict()
    res_data['userId'] = user.userid
    res_data['username'] = user.username
    res_data['phoneNum'] = user.phone
    res_data['signature'] = user.signature
    res_data['headPortraitPath'] = user.icon_url  # default
    res_data['region'] = user.region
    res_data['gender'] = user.gender
    res_data['birthday'] = user.birthday

    return jsonify({'code': 200, 'msg': '注册成功', 'data': res_data})


@login_blueprint.route('/signup', methods=['POST'])
def user_signup():
    data = json.loads(request.get_data(as_text=True))
    phone = data['phoneNum']
    username = data['username']
    password = data['password']

    signature = data['signature']
    region = data['region']
    gender = data['gender']
    birthday = data['birthday']

    if check_phone_exist(phone):
        return jsonify({'code': 401, 'msg': '手机号或邮箱重复', 'data': ''})  # dup phone number
    if check_username_exist(username):
        return jsonify({'code': 402, 'msg': '注册失败', 'data': ''})  # dup username
    create_user(phone, username, password, signature, region, gender, birthday)
    return jsonify({'code': 200, 'msg': '注册成功', 'data': ''})
