from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

#from models import Patient , PatientVisits

app = Flask(__name__)
app.config['SECRET_KEY'] = '09e8a6951e278a87fc7e234913a7c1aa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from doctormohamed import route
