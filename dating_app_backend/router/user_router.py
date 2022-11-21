from flask import Blueprint, request, jsonify, json
from service.user_service import user_add_tags, user_get_tags, check_userid_exist

user_blueprint = Blueprint(
    'user',
    __name__,
    url_prefix='/user'
)


@user_blueprint.route('/setTags', methods=['POST'])
def set_tags():
    data = json.loads(request.get_data(as_text=True))
    user_id = data['userId']
    tags = data['tags']
    image = data['image']

    if not check_userid_exist(user_id):
        return jsonify({'code': 401, 'msg': '设置失败', 'data': ''})  # userid doesn't exist

    # image TODO
    user_add_tags(user_id, tags)
    return jsonify({'code': 200, 'msg': '设置成功', 'data': ''})


@user_blueprint.route('/getTags', methods=['POST'])
def get_tags():
    data = json.loads(request.get_data(as_text=True))
    user_id = data['userId']

    if not check_userid_exist(user_id):
        return jsonify({'code': 401, 'msg': '设置失败', 'data': ''})  # userid doesn't exist

    tags_id = user_get_tags(user_id)
    res_data = dict()
    res_data['tags'] = tags_id
    # print(res_data)
    return jsonify({'code': 200, 'msg': '获取成功', 'data': res_data})
