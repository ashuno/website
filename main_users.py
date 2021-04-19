import flask_login

from data import db_session
from data.users import User
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
        user = User()
        user.name = form['name']
        user.age = form['age']
        user.email = form['email']
        user.set_password(form['password'])
        user.about = form['about']
        # user.hobby = '-4-, -7-, -32-'
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
        # user = session.query(User).filter(User.id == flask_login.current_user.id).first()
        user.name = form['name']
        # !!!!!!user.age = form['age']
        user.email = form['email']
        if len(form['password']) > 0:
            user.set_password(form['password'])
        user.about = form['about']
        # user.hobby = '-4-, -7-, -32-'
        user.gender = form['gender']
        # session.add(user)
        session.commit()
        return True


    # for user in session.query(User).filter(User.hobby.like('%-4-%')):
    #     print(user)
    #     user.about = 'tra ta ta'
    # session.commit()






# def main():
#     db_session.global_init("db/users.sqlite")
#     session = db_session.create_session()
#
#     # user = User()
#     # user.name = "Ridley"
#     # user.age = 21
#     # user.email = "scott_chief@mars.org"
#     # user.set_password("cap")
#     # user.about = 'aaaaaaaaa'
#     # user.hobby = '-4-, -7-, -32-'
#     # user.gender = 'male'
#     # session.add(user)
#     #
#     # session.commit()
#     for user in session.query(User).filter(User.hobby.like('%-4-%')):
#         print(user)
#         user.about = 'tra ta ta'
#     session.commit()
#
#
# if __name__ == '__main__':
#     main()
