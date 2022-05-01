from flask import render_template, url_for, flash, redirect, request 
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post 
from flaskblog import app, db, bcrypt
from flask_login import login_user, current_user,logout_user, login_required

# from turtle import title


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
    # Logout user
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Hash password befor checking for validation 
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode ('utf-8')
        # Create a new Instance of user
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)

        db.session.add(user)
        db.session.commit()
        flash(f'Your acount has been created you are now able to log in', 'success')
        return redirect(url_for('login'))     
    return  render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
       
       # Check if user exist using theire email
        user = User.query.filter_by(email=form.email.data).first()
        # Verifier intered password 
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # Get next (turneray condition)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return  render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

# Restrict user accesibility of pagies 
@app.route("/account")
@login_required 
def account():
    return  render_template('account.html', title='Account')