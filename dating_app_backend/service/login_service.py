from models import User


def check_phone_exist(phone_num):
    if User.query.filter_by(phone=phone_num).count() > 0:
        return True
    else:
        return False


def check_username_exist(name):
    if User.query.filter_by(username=name).count() > 0:
        return True
    else:
        return False


def check_password(phone_num, password):
    user = User.query.filter_by(phone=phone_num).first()
    return user.__check_password__(password)