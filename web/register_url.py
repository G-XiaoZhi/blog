# coding:utf-8
from blog.web.views.index import bp as index_bp


def register_bp(app):
    app.register_blueprint(index_bp)