# coding:utf-8
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class VersionMix(object):
    create_time = db.Column(db.DateTime, default=datetime.now, nullable=False, doc=u"创建时间")
    modify_time = db.Column(db.DateTime, default=datetime.now, nullable=False, doc=u"修改时间")
    version = db.Column(db.Integer, default=1, nullable=False, doc=u"版本号")

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    __mapper_args__ = {
        'version_id_col': version,
    }