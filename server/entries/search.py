# coding: utf-8
from blog.model.entity import Entry


class EntrySearch(object):

    @staticmethod
    def entry_list(page, limit):
        entries = Entry.query.order_by(Entry.create_time.desc()).limit(limit).offset((page-1)*limit).all()
        return entries

    @staticmethod
    def entry_detail(slug):
        entry = Entry.query.filter(Entry.slug == slug).first()
        # entry.tags = []
        return entry