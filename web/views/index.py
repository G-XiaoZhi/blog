# coding:utf-8
from flask import Blueprint, render_template
from flask import request

bp = Blueprint(__name__, __name__)


@bp.route('/')
def index():
    name = request.args.get('name')
    number = request.args.get('number') or 0
    return render_template('homepage.html', name=name, number=number)


@bp.route('/hello/<name>')
def hello(name):
    return "Hello, %s " % name