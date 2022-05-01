from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User  

class RegistrationForm(FlaskForm):
    username = StringField('username', 
                    validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                    validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')

    # User WTF For validating form
    def validate_username(self, username):  
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    # User WTF For validating form
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                    validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])

   # Secure cookie for keeping the user stay loged in for while 
    remember = BooleanField('Remember Me')
    submit = SubmitField('sign up')

 