from flask import Flask
from flask_sqlalchemy import SQLAlchemy

 
## Configurations 
app = Flask(__name__)
app.config['SECRET_KEY'] = '_0ff424c986ca38f387558a452257306522_'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Data base instance 
db = SQLAlchemy(app)

from flaskblog import routes 
