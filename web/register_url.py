# coding:utf-8
from blog.web.views.index import bp as index_bp
from blog.web.views.entries.search import bp as entries_bp


def register_bp(app):
    app.register_blueprint(index_bp)
    app.register_blueprint(entries_bp, url_prefix='/entries')