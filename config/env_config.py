# coding: utf-8
import os
from dotenv import find_dotenv, load_dotenv
from blog.config import InitConfig


class EnvConfig(InitConfig):

    def __init__(self):
        load_dotenv(find_dotenv(), override=True)
        self.set_config()

    def set_config(self):
        self.DB_URL_W = os.environ.get('DB_URL_W')
        self.DEBUG = os.environ.get('DEBUG')

