# coding:utf-8
from blog.common.db_connection import db, VersionMix
from blog.common.utils import slugify


class Tag(db.Model, VersionMix):
    __table_name__ = 'tag'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(64), default='', nullable=False, doc=u'')
    slug = db.Column(db.String(64), default='', unique=True)

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)