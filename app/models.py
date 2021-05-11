from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    isCoach = db.Column(db.Boolean, default=False)
    # subscriptions = db.relationship('Subscription', backref='sub', lazy='dynamic')



    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


# class Subscription(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     dateOfStart = db.Column(db.DateTime, default=datetime.today())
#     dateOfEnd = db.Column(db.DateTime, default=datetime.today() + datetime.timedelta(month=1))
#     status = db.Column(db.Boolean, default=False)
#
#
# class TypeOfSub(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     Description = db.Column(db.String(140))
#     price = db.Column(db.Numeric(5))
#     pool = db.Column(db.Boolean, default=False)
#
#     def __repr__(self):
#         return '<TypeOfSub {}>'.format(self.username)
