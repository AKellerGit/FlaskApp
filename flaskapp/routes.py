from flaskapp.models import User, Post
from flask import render_template, url_for, flash, redirect
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp import app, db, bcrypt
from flask_login import login_user, current_user, logout_user

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
	return render_template('home.html')

#decorators
@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/register", methods=['GET','POST'])
def register():
	#calls RegistrationForm() class from forms.py
	form = RegistrationForm()
	#when form is submitted passes requirements, an account is created
	#and the user is rerouted to home page. A message will appear to inform user
	#the account was created.
	if form.validate_on_submit():
		#hashing password
		hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password = hashed_pw)
		db.session.add(user)
		db.session.commit()
		#end hashing
		flash(f'Account created. Please Log into your account', 'Success')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			#login_user(user, remember=form.remember.data)
			return redirect(url_for('home'))
		else:
			flash(f'Login unsuccessful. Please verify credentials', 'danger')
	return render_template('login.html', form=form)