from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config


app = Flask('Netology')
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=config.SQLITE_URI, SQLALCHEMY_TRACK_MODIFICATIONS=False)
db = SQLAlchemy(app)
