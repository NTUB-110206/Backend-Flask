from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

app.config.from_object('app.setting')

db = SQLAlchemy(app)


from app.model import News

from app.controller import manage