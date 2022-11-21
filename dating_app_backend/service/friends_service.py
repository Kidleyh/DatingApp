import db
from sqlalchemy import null

from models import User, db
from service.user_service import find_user_by_id


def user_like_friend(like_id, liked_id):
    like = find_user_by_id(like_id)
    liked = find_user_by_id(liked_id)
    like.likes.append(liked)
    db.session.commit()


def user_dislike_friend(dislike_id, disliked_id):
    dislike = find_user_by_id(dislike_id)
    disliked = find_user_by_id(disliked_id)
    dislike.dislikes.append(disliked)
    db.session.commit()


# TODO
def find_friend(user_id):
    return User.query.first()
