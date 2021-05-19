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



from app import db
from app.models import Accounting, User, Sub,  Time

# a = Accounting(user_id=1, sub_id=1, status=True)
# a = Accounting.query.get(1)
# db.session.add(a)
# db.session.commit()
# temp = a.user_id
# u = User.query.get(a.user_id)
# print(u.username)
# a.time_id=1
# db.session.add(a)
# db.session.commit()
# print(a.id,a.user_id ,a.sub_id,a.dateOfStart,a.dateOfEnd,a.status,a.time_id)

# ** add person to db wth password
# u = User(username='john', email='john@example.com')
# u.set_password('cat')
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
from app import app

# subs = Sub.query.all()
# for sub in subs:
#     print(sub.id, sub.name, sub.Description, sub.price, sub.pool)
# t = Time(partOfDay='18:00-21:00')
# db.session.add(t)
# db.session.commit()
# time = Time.query.all()
# for tim in time:
#     print(tim.partOfDay)
# if __name__ == '__main__':
#     app.run()
# ##
### Adding/removing coach-status ###
# from app import db
# from app.models import Sub

# s = Sub.query.get(2)
# s = Sub(name="Winter", Description="Time to work!", price=500)
# db.session.delete(s)
# db.session.add(s)
# db.session.commit()
# print(s.id, s.name, s.Description, s.price, s.pool)
# print(s)



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