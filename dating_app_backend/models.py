from db import db
import uuid

# 用户拥有多个标签
user_tag = db.Table('user_tag',
                    db.Column('userid', db.String(50), db.ForeignKey('user.userid'), primary_key=True),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.tag_id'), primary_key=True)
                    )

# 用户偏爱多个标签
user_prefer_tag = db.Table('user_prefer_tag',
                           db.Column('userid', db.String(50), db.ForeignKey('user.userid'), primary_key=True),
                           db.Column('tag_id', db.Integer, db.ForeignKey('tag.tag_id'), primary_key=True)
                           )

user_like = db.Table('user_like',
                     db.Column('like_id', db.String(50), db.ForeignKey('user.userid'), primary_key=True),
                     db.Column('liked_id', db.String(50), db.ForeignKey('user.userid'), primary_key=True)
                     )

user_dislike = db.Table('user_dislike',
                        db.Column('dislike_id', db.String(50), db.ForeignKey('user.userid'), primary_key=True),
                        db.Column('disliked_id', db.String(50), db.ForeignKey('user.userid'), primary_key=True)
                        )


# 用户表
class User(db.Model):
    __tablename__ = 'user'
    userid = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    signature = db.Column(db.String(100), default='')
    region = db.Column(db.String(100), default='')
    gender = db.Column(db.String(50), default='')
    birthday = db.Column(db.String(50), default='')
    icon_url = db.Column(db.String(100), default='')

    tags = db.relationship('Tag', secondary=user_tag, backref=db.backref('users'))
    prefer_tags = db.relationship('Tag', secondary=user_prefer_tag, backref=db.backref('prefer_users'))
    likes = db.relationship('User',
                            secondary=user_like,
                            primaryjoin=(user_like.c.like_id == userid),
                            secondaryjoin=(user_like.c.liked_id == userid),
                            backref=db.backref('liked')
                            )
    dislikes = db.relationship('User',
                               secondary=user_dislike,
                               primaryjoin=(user_dislike.c.dislike_id == userid),
                               secondaryjoin=(user_dislike.c.disliked_id == userid),
                               backref=db.backref('disliked'))

    def __init__(self, phone, username, password):
        self.phone = phone
        self.username = username
        self.password = password
        self.userid = str(uuid.uuid4())
        self.birthday = '2022-01-01'

    def __check_password__(self, password):
        if self.password == password:
            return True
        else:
            return False

    def __get_tags_id__(self):
        tags_id = []
        for tag in self.tags:
            tags_id.append(tag.tag_id)
        return tags_id

    def __get_age__(self):
        if len(self.birthday) < 4:
            return 0
        year = int(self.birthday[0:4])
        return 2022 - year

    def __repr__(self):
        return 'userid: %s, username: %s, phone: %s, signature: %s, region: %s, gender: %s, birthday: %s' \
            .format(self.userid, self.username, self.phone, self.signature, self.region, self.gender, self.birthday)


# 标签表
class Tag(db.Model):
    __tablename__ = 'tag'
    tag_id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(50), unique=True)

    def __init__(self, tag_id, tag_name):
        self.tag_id = tag_id
        self.tag_name = tag_name

    def __repr__(self):
        return 'tag_id: %s, tag_name: %s'.format(self.tag_id, self.tag_name)
