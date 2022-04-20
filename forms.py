from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('username', 
                    validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                    validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                    validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
   # Secure cookie for keeping the user stay loged in for while 
    remember = BooleanField('Remember Me')
    submit = SubmitField('sign up')

 