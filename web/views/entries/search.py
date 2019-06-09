# coding: utf-8

from flask import Blueprint, request, render_template
from blog.server.entries.search import EntrySearch
from blog.server.tag.search import TagSearch

bp = Blueprint(__name__, __name__)


@bp.route('/')
def index():
    page = request.args.get('page')
    limit = request.args.get('limit')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if limit and limit.isdigit():
        limit = 25
    else:
        limit = 25

    entity_list = EntrySearch.entry_list(page, limit)
    return render_template('entries/index.html', object_list=entity_list)


@bp.route('/tags')
def tag_index():
    pass


@bp.route('/tags/detail')
def tag_detail():
    slug = request.args.get('slug')
    tag = TagSearch.tag_detail(slug)
    entries = EntrySearch.entry_list(1,25)
    return render_template('entries/tag_detail.html', tag=tag, object_list=entries)


@bp.route('/slug')
def detail():
    slug = request.args.get('slug')
    entry = EntrySearch.entry_detail(slug)
    return render_template('entries/detail.html', entry=entry)

