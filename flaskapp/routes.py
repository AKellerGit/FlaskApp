from flaskapp.models import User, Post
from flask import render_template, url_for, flash, redirect
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp import app

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