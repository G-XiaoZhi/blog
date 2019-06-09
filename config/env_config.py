# coding: utf-8
import os
from dotenv import find_dotenv, load_dotenv
from blog.config import InitConfig


class EnvConfig(InitConfig):

    def __init__(self):
        load_dotenv(find_dotenv(), override=True)
        self.set_config()

    def set_config(self):
        self.SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
        self.DEBUG = os.environ.get('DEBUG')
        self.SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

