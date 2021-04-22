import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    gender = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    hobby = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return f'''user {self.id} {self.name} :^)'''

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class Hobby(SqlAlchemyBase):
    __tablename__ = 'hobbies'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
