from flask_sqlalchemy import SQLAlchemy
from phillyphoodies import db, login_manager
from flask_login import UserMixin

db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	__tablename__ = 'Users'
	UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	UserName = db.Column(db.String(20), unique=True, nullable=False)
	Email = db.Column(db.String(120), unique=True, nullable=False)
	UserPassword = db.Column(db.String(60), nullable=False)

	def __init__(self, UserName, Email, Password):
		self.UserName = UserName
		self.Email = Email
		self.UserPassword = Password

	def get_id(self):
		return(self.UserID)

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