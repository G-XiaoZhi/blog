# coding: utf-8
from blog.model.tag import Tag


class TagSearch(object):

    @staticmethod
    def entity_list(page, limit):
        entries = Tag.query.order_by(Tag.create_time.desc()).limit(limit).offset((page-1)*limit).all()
        return entries

    @staticmethod
    def tag_detail(slug):
        tag = Tag.query.filter(Tag.slug == slug).first()
        return tag