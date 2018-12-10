from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html', form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)