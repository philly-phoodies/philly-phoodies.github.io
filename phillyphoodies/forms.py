from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import Form, StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from phillyphoodies.models import User

class RegistrationForm(FlaskForm):
	username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('email', validators=[DataRequired(), Email()])
	password = PasswordField('password', validators=[DataRequired()])
	confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(UserName=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a new one.')

	def validate_email(self, email):
		user = User.query.filter_by(Email=email.data).first()
		if user:
			raise ValidationError('That email was taken please choose a new one.')

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('That username is taken. Please choose a new one.')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('That email was taken please choose a new one.')
 
class SearchForm(FlaskForm):
    search = StringField('', validators=[DataRequired()])






    