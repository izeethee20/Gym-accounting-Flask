# from app.models import User
# print(User())
# u = User(username='vmch_')
# db.session.add(u)
# db.session.commit()
# from app.models import User
# user = User.query.filter_by(username="vmch_").first()
            # user1 = User(body=form.user.data, author=current_user)
# user.isCoach = True
# print(user.isCoach)
# u = User.query.get(1)
# p = Post(body='my first post!', author=u)
# db.session.add(p)
# db.session.commit()
# print(u, p)
# print(u.isCoach)
# users = User.query.all()
# for u in users:
#     db.session.delete(u)
# db.session.commit()

# ** add person to db wth password
# u = User(username='john', email='john@example.com')
# u.set_password('cat')
# db.session.add(u)
# db.session.commit()
# **

# * контекст оболочки чтобы добавить экземпляр и модели бд в сеанс оболочки
# from app import app, db
# from app.models import User, Post
#
#
# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User, 'Post': Post}
# *
from sqlalchemy.ext.asyncio import engine

from app.models import Post

Post.__table__.drop()

# if __name__ == '__main__':
#     flask.app()

### Adding/removing coach-status ###

# from app import db
# from app.models import User
#
# user = User.query.filter_by(username='Vlad').first()
#
# db.session.delete(user)
# user.isCoach = True
# user.isCoach = False
# db.session.add(user)
# db.session.commit()
# # user = User.query.filter_by(username='Vlad').first()
#
# print(user.isCoach)
################ # # # ##############