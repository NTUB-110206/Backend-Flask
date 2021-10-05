from app.model.News import News, NewsSchema, Category, CategorySchema
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
    result = Category.query.all()
    print(result)
    output = CategorySchema(many=True).dump(result)
    print(output)
    return {'news': output}
    # return {'news': "create"}


def update():
    return {'news': "update"}
