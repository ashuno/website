import flask_login

from data import db_session
from data.users import User, Hobby
from flask import *
from flask_login import LoginManager

# app = Flask(__name__)
# login_manager = LoginManager()
# login_manager.init_app(app)
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     db_sess = db_session.create_session()
#     return db_sess.query(User).get(user_id)


def reg(form):
    db_session.global_init("db/users.sqlite")
    session = db_session.create_session()
    user = session.query(User).filter(User.email == form['email']).first()
    if user:
        return False
    else:
        sp_id = []
        for k, v in form.items():
            if 'hobby' in k:
                id = k.replace('hobby', '')
                sp_id.append(id)

        hobby_ids = '-'.join(sp_id)
        hobby_ids = '-' + hobby_ids + '-'

        user = User()
        user.name = form['name']
        user.age = form['age']
        user.email = form['email']
        user.set_password(form['password'])
        user.about = form['about']
        user.hobby = hobby_ids
        user.gender = form['gender']
        session.add(user)
        session.commit()
        return True


def login_user(form):
    db_session.global_init("db/users.sqlite")
    session = db_session.create_session()
    user = session.query(User).filter(User.email == form['email']).first()
    if user.check_password(form['password']):
        return True
    else:
        return False


def editing(form):
    db_session.global_init("db/users.sqlite")
    session = db_session.create_session()

    user = session.query(User).filter(User.email == form['email']).first()
    if user and user != flask_login.current_user:
        return False
    else:
        user.name = form['name']
        user.age = form['age']
        user.email = form['email']
        if len(form['password']) > 0:
            user.set_password(form['password'])
        user.about = form['about']
        sp_id = []
        for k, v in form.items():
            if 'hobby' in k:
                id = k.replace('hobby', '')
                sp_id.append(id)
        hobby_ids = '-'.join(sp_id)
        hobby_ids = '-' + hobby_ids + '-'

        user.hobby = hobby_ids
        user.gender = form['gender']
        session.commit()
        return True


def init_hobbies():
    db_session.global_init("db/users.sqlite")
    session = db_session.create_session()
    hobby = Hobby()
    hobby.name = 'video_editing'
    hobby.descr = 'Видеомонтаж'

    session.add(hobby)
    session.commit()
    hobby = Hobby()

    hobby.descr = 'Дизайн'
    session.add(hobby)
    session.commit()
    hobby = Hobby()
    hobby.descr = 'Животные'
    session.add(hobby)
    session.commit()
    hobby = Hobby()
    hobby.descr = 'Игра на музыкальных инструментах'
    session.add(hobby)
    session.commit()
    hobby = Hobby()
    hobby.descr = 'Игры на компьютерах и приставках'
    session.add(hobby)
    session.commit()
    hobby = Hobby()
    hobby.descr = 'Иностранные языки'
    session.add(hobby)
    session.commit()
    hobby = Hobby()
    hobby.descr = 'Коллекционирование'
    session.add(hobby)
    session.commit()
    hobby = Hobby()
    hobby.descr = 'Моделирование'
    session.add(hobby)
    session.commit()
    hobby = Hobby()
    hobby.descr = 'Пение'
    session.add(hobby)
    session.commit()
    hobby = Hobby()
    hobby.descr = 'Программирование'
    session.add(hobby)
    session.commit()
    hobby = Hobby()
    hobby.descr = 'Рисование'
    session.add(hobby)
    session.commit()
    hobby = Hobby()
    hobby.descr = 'Спорт'
    session.add(hobby)
    session.commit()


def get_hobbies():
    db_session.global_init("db/users.sqlite")
    session = db_session.create_session()
    return session.query(Hobby).all()


def top_hobbies():

    db_session.global_init("db/users.sqlite")
    session = db_session.create_session()
    hobbies = get_hobbies()
    sp = []
    for hobby in hobbies:
        user_num = session.query(User).filter(User.hobby.like('%-' + str(hobby.id) + '-%')).count()
        sp.append([hobby.name, user_num])
    sp = sorted(sp, key=lambda x: x[1], reverse=True)
    return sp
