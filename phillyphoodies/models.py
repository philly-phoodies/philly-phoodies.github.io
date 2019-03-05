from phillyphoodies import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)

	# def __repr__(self):
		# return '<User %r>' % ((self.usename), (self.email), (self.image_file))

class Restaurants(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	description = db.Column(db.Text, nullable=False)
	keywords = db.Column(db.Text, nullable=False)
	address = db.Column(db.String(250), unique=True, nullable=False)
	price = db.Column(db.Integer, nullable=False)
	link = db.Column(db.String(250), unique=True, nullable=False)

	# def __repr__(self):
		# return f"Restaurants('{self.title}', '{self.description}', '{self.address}', '{self.price}', '{self.link}')"