from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    # create the app
    _app = Flask(__name__)

    # set app config
    _app.debug = True

    # init db
    db = SQLAlchemy()
    db.init_app(_app)

    return _app


app = create_app()
