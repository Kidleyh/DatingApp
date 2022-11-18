from db import db


# 用户表
class User(db.Model):
    __tablename__ = 'user'
    userid = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    signature = db.Column(db.String(100))
    region = db.Column(db.String(100))
    gender = db.Column(db.String(50))
    birthday = db.Column(db.String(50))
    icon_url = db.Column(db.String(100))

    tags = db.relationship('Tag', secondary='user_tag', backref=db.backref('users'))
    prefer_tags = db.relationship('Tag', secondary='user_prefer_tag', backref=db.backref('prefer_users'))

    def __init__(self, phone, username, email):
        self.phone = phone
        self.username = username
        self.email = email

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
