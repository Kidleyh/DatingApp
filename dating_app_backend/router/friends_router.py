from flask import Blueprint, request, jsonify, json

from service.user_service import check_userid_exist
from service.friends_service import find_friend, user_like_friend, user_dislike_friend

friends_blueprint = Blueprint(
    'friends',
    __name__,
    url_prefix='/friends'
)


@friends_blueprint.route('/likeFriend', methods=['POST'])
def like_friend():
    data = json.loads(request.get_data(as_text=True))
    like_id = data['userId']
    liked_id = data['likeUserId']

    if not check_userid_exist(like_id):
        return jsonify({'code': 401, 'msg': '失败', 'data': ''})  # userid doesn't exist
    if not check_userid_exist(liked_id):
        return jsonify({'code': 401, 'msg': '失败', 'data': ''})  # userid doesn't exist
    user_like_friend(like_id, liked_id)
    return jsonify({'code': 200, 'msg': '成功', 'data': ''})


@friends_blueprint.route('/dislikeFriend', methods=['POST'])
def dislike_friend():
    data = json.loads(request.get_data(as_text=True))
    dislike_id = data['userId']
    disliked_id = data['dislikeUserId']

    if not check_userid_exist(dislike_id):
        return jsonify({'code': 401, 'msg': '失败', 'data': ''})  # userid doesn't exist
    if not check_userid_exist(disliked_id):
        return jsonify({'code': 401, 'msg': '失败', 'data': ''})  # userid doesn't exist
    user_dislike_friend(dislike_id, disliked_id)
    return jsonify({'code': 200, 'msg': '成功', 'data': ''})


@friends_blueprint.route('/getFriend', methods=['POST'])
def get_friend():
    data = json.loads(request.get_data(as_text=True))
    user_id = data['userId']

    if not check_userid_exist(user_id):
        return jsonify({'code': 401, 'msg': '设置失败', 'data': ''})  # userid doesn't exist

    user = find_friend()
    res_data = dict()
    res_data['userId'] = user.userid
    res_data['username'] = user.username
    res_data['phoneNum'] = user.phone
    res_data['signature'] = user.signature
    res_data['region'] = user.region
    res_data['gender'] = user.gender
    res_data['age'] = user.__get_age__()
    res_data['image'] = user.icon_url
    res_data['tags'] = user.__get_tags_id__()
    return jsonify({'code': 200, 'msg': '获取成功', 'data': res_data})
