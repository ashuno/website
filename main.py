import flask_login

from main_users import *
from flask_login import LoginManager, login_user, login_required
from data.users import LoginForm
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    db_session.global_init("db/users.sqlite")
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    main_style = url_for('static', filename='css/main_style.css')
    style = url_for('static', filename='css/style.css')
    button_style = url_for('static', filename='css/button_style.css')
    text_style = url_for('static', filename='css/text_style.css')
    ph_style = url_for('static', filename='css/ph_style.css')

    return render_template('template_bg.html', main_style=main_style, style=style, button_style=button_style, text_style=text_style, ph_style=ph_style)


@app.route('/register', methods=['POST', 'GET'])
def register():
    main_style = url_for('static', filename='css/main_style.css')
    button_style2 = url_for('static', filename='css/button_style.css')
    text_style2 = url_for('static', filename='css/text_style2.css')
    an_style = url_for('static', filename='css/an_style.css')
    checkbox_style = url_for('static', filename='css/checkbox_style.css')
    radio_checkbox_style = url_for('static', filename='css/radio_checkbox_style.css')

    if request.method == 'GET':
        return render_template('register_template.html', main_style=main_style, text_style2=text_style2,
                               an_style=an_style, button_style2=button_style2, checkbox_style=checkbox_style,
                               radio_checkbox_style=radio_checkbox_style, email_exists=False)
    else:
        if not reg(request.form):
            return render_template('register_template.html', main_style=main_style, text_style2=text_style2,
                                   an_style=an_style, button_style2=button_style2, checkbox_style=checkbox_style,
                                   radio_checkbox_style=radio_checkbox_style, email_exists=True)

        return redirect('/choice')


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     main_style = url_for('static', filename='css/main_style.css')
#     button_style2 = url_for('static', filename='css/button_style.css')
#     text_style = url_for('static', filename='css/text_style.css')
#     an_style = url_for('static', filename='css/an_style.css')
#     checkbox_style = url_for('static', filename='css/checkbox_style.css')
#     radio_checkbox_style = url_for('static', filename='css/radio_checkbox_style.css')
#     if request.method == 'GET':
#         return render_template('login_template.html', main_style=main_style, text_style=text_style, an_style=an_style,
#                                button_style2=button_style2, checkbox_style=checkbox_style,
#                                radio_checkbox_style=radio_checkbox_style, email_or_password_doesnt_match=False)
#     else:
#         if not login_user(request.form):
#             return render_template('login_template.html', main_style=main_style, text_style=text_style,
#                                    an_style=an_style,
#                                    button_style2=button_style2, checkbox_style=checkbox_style,
#                                    radio_checkbox_style=radio_checkbox_style, email_or_password_doesnt_match=True)
#         return redirect('/choice')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_session.global_init("db/users.sqlite")
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/choice")
        return render_template('login_form2.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login_form2.html', title='Авторизация', form=form)


@app.route('/me', methods=['POST', 'GET'])
def profile():
    print(flask_login.current_user)
    main_style = url_for('static', filename='css/main_style.css')
    an_style = url_for('static', filename='css/an_style.css')
    ph_style = url_for('static', filename='css/ph_style.css')
    text_style2 = url_for('static', filename='css/text_style2.css')
    button_style2 = url_for('static', filename='css/button_style2.css')

    if request.method == 'GET':
        return render_template('profile_template.html', main_style=main_style, an_style=an_style, ph_style=ph_style, text_style2=text_style2, button_style2=button_style2)
    else:

        return redirect('/changing_profile')


@app.route('/choice')
def choice():
    main_style2 = url_for('static', filename='css/main_style2.css')
    button_style2 = url_for('static', filename='css/button_style2.css')
    return render_template('after_reg.html', button_style2=button_style2, main_style2=main_style2)


@app.route('/people')
def people():
    main_style = url_for('static', filename='css/main_style.css')

    return render_template('people_temp.html',  main_style=main_style)


@app.route('/changing_profile', methods=['POST', 'GET'])
def changing_profile():
    if not flask_login.current_user.is_authenticated:
        return '>:('
    main_style = url_for('static', filename='css/main_style.css')
    button_style2 = url_for('static', filename='css/button_style.css')
    text_style2 = url_for('static', filename='css/text_style2.css')
    an_style = url_for('static', filename='css/an_style.css')
    checkbox_style = url_for('static', filename='css/checkbox_style.css')
    radio_checkbox_style = url_for('static', filename='css/radio_checkbox_style.css')


    name = flask_login.current_user.name
    email = flask_login.current_user.email


    if request.method == 'GET':

        return render_template('changing_profile.html', name=name, email=email, main_style=main_style, text_style2=text_style2,
                               an_style=an_style, button_style2=button_style2, checkbox_style=checkbox_style,
                               radio_checkbox_style=radio_checkbox_style, email_exists=False)
    else:
        if not editing(request.form):
            return render_template('changing_profile.html', main_style=main_style, text_style2=text_style2,
                                   an_style=an_style, button_style2=button_style2, checkbox_style=checkbox_style,
                                   radio_checkbox_style=radio_checkbox_style, email_exists=True)
        return redirect('/choice')


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
