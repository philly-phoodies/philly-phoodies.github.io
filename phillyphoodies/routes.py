from flask import render_template, url_for, flash, redirect, request, jsonify
from phillyphoodies import app, db, bcrypt
from phillyphoodies.models import User, Restaurant, Food
from phillyphoodies.forms import RegistrationForm, LoginForm, SearchForm, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy.ext.declarative import DeclarativeMeta
import json

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', post='post')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(UserName=form.username.data, Email=form.email.data, Password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your accound has been created, you are now able to login', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(Email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.UserPassword, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
	form = UpdateAccountForm()
	return render_template('account.html', title='Account', form=form)


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields
        return json.JSONEncoder.default(self, obj)

@app.route("/", methods = ["GET"])
def homeresult():
	users = db.session.query(Users)
	results = Users.query.all()
	return json.dumps(results, cls=AlchemyEncoder)

@app.route("/search", methods=["GET", "POST"])
def search():
	searchbar = request.form.get("searchbar")

	return "searchitem : %s"  %(searchbar)

@app.route("/searchrestaurant/<restaurant>", methods = ["GET"])
def searchrestaurant(restaurant):
	results = db.session.query(Restaurant).filter(Restaurant.restaurantname==restaurant).first()
	return json.dumps(results, cls=AlchemyEncoder)


