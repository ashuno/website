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


@app.route('/register')
def register():
    main_style = url_for('static', filename='css/main_style.css')

    return render_template('register_template.html', main_style=main_style)


@app.route('/login')
def login():
    main_style = url_for('static', filename='css/main_style.css')

    return render_template('register_template.html', main_style=main_style)

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
