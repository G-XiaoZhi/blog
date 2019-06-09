import re


def slugify(s):
    return re.sub('[^\w]+', '-', s).lower()


if __name__ == "__main__":
    print slugify("Flask test")