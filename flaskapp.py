from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://site.db'

db = SQLAlchemy(app)



@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/register", methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'Success')
		return redirect(url_for('home'))

	return render_template('register.html', form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)