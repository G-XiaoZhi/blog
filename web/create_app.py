from flask import Flask
from blog.common.db_connection import db
from blog.config.env_config import EnvConfig
from blog.web.register_url import register_bp


def create_app():
    # create the app
    _app = Flask(__name__)
    cnf = EnvConfig()
    _app.config.from_object(cnf)

    # set app config
    _app.debug = True

    # init db
    db.init_app(_app)

    # register blueprint
    register_bp(_app)

    return _app


app = create_app()
