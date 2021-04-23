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
    top = top_hobbies()
    return render_template('template_bg.html', top=top,  main_style=main_style, style=style, button_style=button_style, text_style=text_style, ph_style=ph_style)


@app.route('/register', methods=['POST', 'GET'])
def register():
    main_style = url_for('static', filename='css/main_style.css')
    button_style2 = url_for('static', filename='css/button_style.css')
    text_style2 = url_for('static', filename='css/text_style2.css')
    an_style = url_for('static', filename='css/an_style.css')
    checkbox_style = url_for('static', filename='css/checkbox_style.css')
    radio_checkbox_style = url_for('static', filename='css/radio_checkbox_style.css')
    hobbies = get_hobbies()
    if request.method == 'GET':
        return render_template('register_template.html', hobbies=hobbies, main_style=main_style, text_style2=text_style2,
                               an_style=an_style, button_style2=button_style2, checkbox_style=checkbox_style,
                               radio_checkbox_style=radio_checkbox_style, email_exists=False)
    else:
        if not reg(request.form):
            return render_template('register_template.html', hobbies=hobbies, main_style=main_style, text_style2=text_style2,
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
    main_style = url_for('static', filename='css/main_style.css')
    an_style = url_for('static', filename='css/an_style.css')

    if form.validate_on_submit():
        db_session.global_init("db/users.sqlite")
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/choice")
        return render_template('login_form2.html',
                               message="Неправильный логин или пароль",
                               form=form, main_style=main_style, an_style=an_style)
    return render_template('login_form2.html', title='Авторизация', form=form)


@app.route('/profile/<user_id>', methods=['POST', 'GET'])
def profile(user_id):
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
    curr_user_id = flask_login.current_user.id

    main_style2 = url_for('static', filename='css/main_style2.css')
    button_style2 = url_for('static', filename='css/button_style2.css')
    return render_template('after_reg.html', curr_user_id=curr_user_id, button_style2=button_style2, main_style2=main_style2)


@app.route('/people')
def people():
    main_style = url_for('static', filename='css/main_style.css')
    act_table_style = url_for('static', filename='css/act_table_style.css')
    top = top_hobbies()
    return render_template('int_table.html', top=top, main_style=main_style, act_table_style=act_table_style)


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
    gender = flask_login.current_user.gender
    age = flask_login.current_user.age
    hobbies = get_hobbies()
    hobby_ids = flask_login.current_user.hobby.split('-')
    if request.method == 'GET':
        return render_template('changing_profile.html', hobby_ids=hobby_ids, hobbies=hobbies, age=age, gender=gender, name=name, email=email,
                               main_style=main_style, text_style2=text_style2, an_style=an_style,
                               button_style2=button_style2, checkbox_style=checkbox_style,
                               radio_checkbox_style=radio_checkbox_style, email_exists=False)
    else:
        if not editing(request.form):
            return render_template('changing_profile.html', hobby_ids=hobby_ids, hobbies=hobbies, age=age, gender=gender,
                                   main_style=main_style, text_style2=text_style2,
                                   an_style=an_style, button_style2=button_style2, checkbox_style=checkbox_style,
                                   radio_checkbox_style=radio_checkbox_style, email_exists=True)
        return redirect('/choice')


@app.route('/users_with_hobby/<hobby_id>')
def users_with_hobby(hobby_id):
    if not flask_login.current_user.is_authenticated:
        return redirect('/register')
    users_sp = get_user_by_hobby(hobby_id)
    main_style = url_for('static', filename='css/main_style.css')
    act_table_style = url_for('static', filename='css/act_table_style.css')

    return render_template('users_with_hobby.html', users_sp=users_sp, act_table_style=act_table_style, main_style=main_style)


if __name__ == '__main__':
    top_hobbies()
    # init_hobbies()
    app.run(port=8080, host='0.0.0.0')
