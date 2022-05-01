import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

 
## Configurations 
app = Flask(__name__)
app.config['SECRET_KEY'] = '_0ff424c986ca38f387558a452257306522_'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Data base instance 
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
# Initailize Bcrypt for hashing  password 
login_manager = LoginManager(app)
login_manager.login_view = 'login' 
login_manager.login_message_category = 'info'

# setting for login requered 

from flaskblog import routes 
