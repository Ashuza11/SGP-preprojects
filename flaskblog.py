from datetime import datetime
from crypt import methods
import email
from email.policy import default
from turtle import title
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
 
## Configurations 
app = Flask(__name__)
app.config['SECRET_KEY'] = '_0ff424c986ca38f387558a452257306522_'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Data base instance 
db = SQLAlchemy(app)

## Database Model (user's table)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True) # 1 to many relationship with Post

    # Magical method for representing a class object
    def __repr__(self):
        return f"User('{self.username}, {self.email}, {self.image_file}')"



## Database Model (Post's table)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Magical method for representing a class object
    def __repr__(self):
        return f"User('{self.title}, {self.date_posted}')"




# Data bse example 
posts = [ 
    {
        'author': 'M ashuza',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2022'
    },
    {
        'author': 'Daid alse',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 23, 2022'
    }
]
   

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))     
    return  render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return  render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)