###adding subs###
from app.models import Sub, Accounting, Time
from app import db
#
# sub = Sub(name='Semi-monthly-standard', Description='''Price: 300
#                                              Age: any
#                                              Duration: 14 days
#                                              Pool: no''', price=300, pool=False)
# db.session.add(sub)
# db.session.commit()
# ###edit###
# s = Sub.query.get(3)
# s.Description = "\n           Price - 650\n           Age - any\n           Duration - 28 days\n           Pool - included"
# s.Description = "\n           Price - 500\n           Age - any\n           Duration - 28 days\n           Pool - no"
# s.Description = "           Price - 300\n           Age - any\n           Duration - 14 days\n           Pool - no"
# s.pool = False
# print(s.Description, s.name)
######################


# times = [1, 2, 3, 4]
# t = Time.query.all()
# for i in times:
#     print(t[i-1].partOfDay)
# a = Accounting.query.get(2)
# print(a.user_id, a.time_id, a.coach_id)
# for i in a:
#     if i.user_id == 3:
#         subIs = True
#         curr_a = i
#         curr_a.time_id=4
#         temp = curr_a.time_id
#         print(temp)
#         t = Time.query.get(temp)
#         print(t.id)
# te = Time.query.all()
# for i in te:
#     print(i.id,i.partOfDay)
###adding time###
# from app import db
# from app.models import Time
#
# time = Time(partOfDay='18:00-21:00')
# db.session.add(time)
# db.session.commit()
#####################


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
import datetime

from app import db
# from app.models import Accounting, User, Sub,  Time

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
# from app.models import Accounting
# sub_id=3
# dateTemp = input().format(datetime)
# dateS = datetime.datetime.strptime(dateTemp, "%d-%m-%Y")
# if sub_id == 3:
#     dateE = dateS + datetime.timedelta(days=14)
# else:
#     dateE = dateS + datetime.timedelta(days=28)
# data = Accounting(user_id=1, sub_id=sub_id, dateOfStart=dateS, dateOfEnd=dateE, status=True, time_id=2, coach_id=1)
# print(data.dateOfStart, data.dateOfEnd, data.time_id)
# from app.models import Accounting
#
# a = Accounting.query.all()
# for i in a:
#     print(i.id, i.dateOfStart, i.dateOfEnd, i.user_id)



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
# date1 = input().format(datetime)
# dateS = datetime.datetime.strptime(date1, "%m/%d/%y")
# dateE = dateS + datetime.timedelta(days=28)
# data = Accounting(user_id=1, sub_id=2, dateOfStart=dateS, dateOfEnd=dateE, status=True, time_id=3)
# print(data.dateOfStart, data.dateOfEnd, data.status)# coaches = User.query.all()
# for co in coaches:
#     if co.isCoach==True:
#         print(co.username)




# data = Accounting.query.all()
# for i in data:
#     print(i.status, i.id)



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