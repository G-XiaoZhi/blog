import re


def slugify(s):
    return re.sub('[^\w]+', '-', s).lower()