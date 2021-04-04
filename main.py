from flask import *


app = Flask(__name__)


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
    text_style = url_for('static', filename='css/text_style.css')
    an_style = url_for('static', filename='css/an_style.css')
    checkbox_style = url_for('static', filename='css/checkbox_style.css')
    radio_checkbox_style = url_for('static', filename='css/radio_checkbox_style.css')
    if request.method == 'GET':

        return render_template('register_template.html', main_style=main_style, text_style=text_style, an_style=an_style, button_style2=button_style2, checkbox_style=checkbox_style, radio_checkbox_style=radio_checkbox_style)
    else:
        print(request.form)
        return redirect('/me')


@app.route('/login', methods=['POST', 'GET'])
def login():
    main_style = url_for('static', filename='css/main_style.css')
    button_style2 = url_for('static', filename='css/button_style.css')
    text_style = url_for('static', filename='css/text_style.css')
    an_style = url_for('static', filename='css/an_style.css')
    checkbox_style = url_for('static', filename='css/checkbox_style.css')
    radio_checkbox_style = url_for('static', filename='css/radio_checkbox_style.css')
    if request.method == 'GET':

        return render_template('login_template.html', main_style=main_style, text_style=text_style, an_style=an_style,
                           button_style2=button_style2, checkbox_style=checkbox_style,
                           radio_checkbox_style=radio_checkbox_style)
    else:
        print(request.form)
        return redirect('/me')


@app.route('/me')
def profile():
    main_style = url_for('static', filename='css/main_style.css')
    an_style = url_for('static', filename='css/an_style.css')
    ph_style = url_for('static', filename='css/ph_style.css')
    if request.method == 'GET':
        return render_template('profile_template.html', main_style=main_style, an_style=an_style, ph_style=ph_style)
    else:
        return "hi"


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
