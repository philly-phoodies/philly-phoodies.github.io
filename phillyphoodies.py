from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, SearchForm


from dbconnect import connection

app = Flask(__name__)

app.config['SECRET_KEY'] = '09ijdh5h4987hfbc'

post = [ 
	{
		'author': 'Katie Miller',
		'titel': 'blog Post 1',
		'content': 'First Blog Post',
		'date_posted': 'Febuary 25th, 2019'
	},
	{
		'author': 'Brett Batcherlor',
		'titel': 'blog Post 2',
		'content': 'Second Blog Post',
		'date_posted': 'Febuary 26th, 2019'
	}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', post=post)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash('Account created for {form.username.data}', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.emial.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check usename and password', 'danger')
	return render_template('login.html', title='Login', form=form)

@app.route("/search", methods=['GET', 'POST'])
def search():
    search = SearchForm(request.form)
    # if request.method == 'POST':
        # return search_results(search)
    return render_template('search.html', form=search)

if __name__ == '__main__':
	app.run(debug=True)