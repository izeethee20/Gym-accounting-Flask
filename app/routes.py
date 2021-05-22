# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, date
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app
from forms import LoginForm, EditProfileForm, CoachIdentifierForm, PayForm
from flask_login import current_user, login_user, login_required
from app.models import User, Sub, Time, Accounting
from flask_login import logout_user
from app import db
from forms import RegistrationForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
@login_required
def home():
    subIs = False
    coach_check = False
    u = User.query.get(current_user.id)
    if u.isCoach:
        coach_check = True
    a = Accounting.query.all()
    for i in a:
        if i.user_id == current_user.id:
            subIs = True
    return render_template('home.html', title="Home", subIs=subIs, coach_check=coach_check)


@app.route('/catalog')
@login_required
def catalog():
    subs = Sub.query.all()
    return render_template('catalog.html', title='Home', subs=subs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('home')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('catalog'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('catalog'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    a = Accounting.query.all()
    for i in a:
        if i.user_id == current_user.id:
            subIs = True
            curr_a = i
            temp = curr_a.time_id
            t = Time.query.get(temp)
            s = Sub.query.get(curr_a.sub_id)
            users = User.query.all()
            trainer_id = curr_a.coach_id
            for j in users:
                if trainer_id == j.id:
                    trainer = j.username
            return render_template('user.html', user=user, subIs=subIs, curr_a=curr_a, s=s, t=t, trainer=trainer)
    return render_template('user.html', user=user)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    subIs = False
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    a = Accounting.query.all()
    for i in a:
        if i.user_id == current_user.id:
            subIs = True
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form, subIs=subIs)


@app.route('/coach_identifier', methods=['GET', 'POST'])
@login_required
def coach_identifier():
    form = CoachIdentifierForm()
    if form.validate_on_submit():
        if form.coach_check.data == "54321":
            user = User.query.filter_by(username=current_user.username).first()
            db.session.delete(user)
            user.isCoach = True
            db.session.add(user)
            db.session.commit()
            flash('Now we know that you are a coach :)')
            return redirect(url_for('home'))
    return render_template('coach_identifier.html', title='Coach identifier', form=form)


@app.route('/choose_time', methods=['GET', 'POST'])
@login_required
def choose_time():
    sub_id = request.args.get('sub_id')
    sub = Sub.query.filter_by(id=sub_id).first()
    times = Time.query.all()
    temp = User.query.all()
    return render_template('choose_time.html', sub=sub, times=times, coaches=temp, sub_id=sub_id)


@app.route('/coach_room', methods=['GET', 'POST'])
@login_required
def coach_room():
    trainings = []
    times = []
    a = Accounting.query.all()
    for i in a:
        if i.coach_id == current_user.id:
            if i.dateOfStart < datetime.today() < i.dateOfEnd:
                trainings.append(i.time_id)
                training = sorted(trainings)
    for g in training:
        temp = Time.query.get(g)
        times.append(temp.partOfDay)
    return render_template('coach_room.html', title='Coach room', trainings=training, times=times)


@app.route('/about_us')
def about_us():
    subIs = False
    a = Accounting.query.all()
    for i in a:
        if i.user_id == current_user.id:
            subIs = True
    return render_template('about_us.html', title="About us", subIs=subIs)


@app.route('/confirm')
def confirm():
    status = request.args.get('st')
    id = request.args.get('id')
    sub_id = request.args.get('sub_id')
    time_id = request.args.get('time_id')
    res = User.query.all()
    sub = Sub.query.get(sub_id)
    time = Time.query.get(time_id)
    return render_template('confirm.html', title='Confirmation', data=res, status=status, id_time=id, sub_id=sub_id, time_id=time_id, sub=sub, time=time)


@app.route('/payment', methods=['GET', 'POST'])
@login_required
def payment():
    form = PayForm()
    time_id = request.args.get('time_id')
    coach_id = request.args.get('coach_id')
    sub_id = request.args.get('sub_id')
    sub = Sub.query.get(sub_id)
    time = Time.query.get(time_id)
    coach = User.query.get(coach_id)
    if request.method == 'POST':
        dateTemp = str(form.DateOfStart.data)
        dateS = datetime.strptime(dateTemp, "%Y-%m-%d").date()
        if sub_id == 3:
            dateE = dateS + timedelta(days=14)
        else:
            dateE = dateS + timedelta(days=28)
        data = Accounting(user_id=current_user.id, sub_id=sub_id, dateOfStart=dateS, dateOfEnd=dateE, status=True,
                          time_id=time_id, coach_id=coach_id)
        db.session.add(data)
        db.session.commit()
        flash('Congratulations, you have the subscription!')
        return redirect(url_for('home'))
    return render_template('payment.html', time_id=time_id, coach_id=coach_id, form=form, sub_id=sub_id, sub=sub, time=time, coach=coach)


@app.route('/info')
@login_required
def info():
    sub_id = request.args.get('sub_id')
    s = Sub.query.get(sub_id)
    return render_template('info.html', sub=s)
