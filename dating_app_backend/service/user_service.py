from models import User, Tag, user_tag, user_prefer_tag, db


def create_user(phone, username, password, signature, region, gender, birthday):
    user = User(phone, username, password)
    user.signature = signature
    user.region = region
    user.gender = gender
    user.birthday = birthday
    db.session.add(user)
    db.session.commit()


def find_user_by_phone(phone_num):
    return User.query.filter_by(phone=phone_num).first()


def find_user_by_id(id_user):
    return User.query.filter_by(userid=id_user).first()


def find_tag_by_id(id_tag):
    return Tag.query.filter_by(tag_id=id_tag).first()


def user_add_tags(user_id, tags):
    user = find_user_by_id(user_id)
    for tag_id in tags:
        tag = find_tag_by_id(tag_id)
        user.tags.append(tag)
    db.session.commit()


def user_get_tags(user_id):
    user = find_user_by_id(user_id)
    return user.__get_tags_id__()


def check_userid_exist(user_id):
    if User.query.filter_by(userid=user_id).count() > 0:
        return True
    else:
        return False
