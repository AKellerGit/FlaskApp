#intialize application and brings different components together

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

#routes import here to avoid circular importing!
from flaskapp import routes