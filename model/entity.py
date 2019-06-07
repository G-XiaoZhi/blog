# coding:utf-8
from blog.common.db_connection import db, VersionMix
from blog.common.utils import slugify


class Entity(db.Model, VersionMix):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), doc=u"博客标题")
    slug = db.Column(db.String(64), unique=True, doc=u"标签")
    body = db.Column(db.Text, doc=u"博客内容")

    def __init__(self, *args, **kwargs):
        super(Entity, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        # 生成标签
        self.slug = slugify(self.title) if self.title else ''