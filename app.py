from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from form import LoginForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap5(app)


@app.route('/')
def handle_form():  # put application's code here
    form = LoginForm()
    return render_template("handle_page.html", form=form)


@app.route('/wtf_form')
def wtf_form():  # put application's code here
    form = LoginForm()
    return render_template("wtf_form_page.html", form=form)


@app.route('/quick_form')
def quick_form():  # put application's code here
    form = LoginForm()
    return render_template("quick_form_page.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
