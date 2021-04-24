import flask_login

from data import db_session
from data.users import User, Hobby


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
        sp.append([hobby.id, hobby.name, user_num])
    sp = sorted(sp, key=lambda x: x[2], reverse=True)
    return sp


def get_user_by_hobby(hobby_id):
    db_session.global_init("db/users.sqlite")
    session = db_session.create_session()
    users = session.query(User).filter(User.hobby.like('%-' + str(hobby_id) + '-%')).all()
    return users


def get_hobby_by_id(hobby_id):
    db_session.global_init("db/users.sqlite")
    session = db_session.create_session()
    hobby = session.query(Hobby).filter(Hobby.id == hobby_id).first()
    return hobby


def get_user_by_id(user_id):
    db_session.global_init("db/users.sqlite")
    session = db_session.create_session()
    user = session.query(User).filter(User.id == user_id).first()
    return user

