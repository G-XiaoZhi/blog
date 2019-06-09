# coding:utf-8
from blog.common.db_connection import db, VersionMix
from blog.common.utils import slugify
from blog.model.tag import Tag


entry_tags = db.Table('entry_tags',
                      db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                      db.Column('entry_id', db.Integer, db.ForeignKey('entry.id')))


class Entry(db.Model, VersionMix):
    __table_name__ = "entry"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), doc=u"博客标题")
    slug = db.Column(db.String(64), unique=True, doc=u"标签")
    body = db.Column(db.Text, doc=u"博客内容")

    tags = db.relationship('Tag', secondary=entry_tags,
                           backref=db.backref('entries', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(Entry, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        # 生成标签
        self.slug = slugify(self.title) if self.title else ''
