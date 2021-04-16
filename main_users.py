from data import db_session
from data.users import User
from flask import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def reg(form):
    db_session.global_init("db/users.sqlite")
    session = db_session.create_session()

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
