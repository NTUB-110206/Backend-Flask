from app.model.News import News, NewsSchema
import re


def read(limit):
    limit = int(re.sub(r'\D', "", limit))
    if limit is not None:
        result = News.query.limit(limit).all()
    else:
        result = News.query.all()
    output = NewsSchema(many=True).dump(result)

    return {'news': output}


def create():
    return {'news': "create"}


def update():
    return {'news': "update"}
