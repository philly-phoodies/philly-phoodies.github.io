from flask_sqlalchemy import SQLAlchemy
from phillyphoodies import db, login_manager
from flask_login import UserMixin

db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	__tablename__ = 'Users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	location = db.Column(db.String(128), nullable=False)

	def __init__(self, id, username, email, image_file, password, location):
		self.id = id
		self.username = username
		self.email = email
		self.image_file = image_file
		self.password = password
		self.location = location

class Restaurant(db.Model):
	__tablename__ = "Restaurant"
	restaurantid = db.Column(db.Integer, primary_key=True, autoincrement=True)
	restaurantname = db.Column(db.String(128), nullable=False)
	address = db.Column(db.String(128))
	state = db.Column(db.String(128))
	pricepoint = db.Column(db.Integer)
	foodtypeid = db.Column(db.Integer, db.ForeignKey('Typefood.foodtypeid'), nullable=False)

	def __init__(self, restaurantidid, name, address, state, pricepoint, foodtypeid):
		self.restaurantidid = restaurantidid
		self.name = name
		self.address = address
		self.state = state
		self.pricepoint = pricepoint
		self.foodtypeid = foodtypeid


class Food(db.Model):
	__tablename__ = "Food"
	foodid = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), nullable=False)
	restaurantidid = db.Column(db.Integer, db.ForeignKey('Restaurant.restaurantidid'), nullable=False, primary_key=True)

	def __init__(self, foodid, name, restaurantidid):
		self.foodid = foodid
		self.name = name
		self.restaurantidid = restaurantidid