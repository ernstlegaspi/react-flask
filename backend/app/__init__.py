from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SECRET_KEY'] = 'mysecretkey'

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

if __name__ == '__main__':
	app.run(debug = True)

from app.models import models
from app.routes import routes
