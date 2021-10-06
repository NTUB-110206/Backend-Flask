from sqlalchemy import desc
from app.model.News import News, NewsSchema
import re


def read(args):
    result = News.query.order_by(desc('news_datetime'))
    news_id_filter = args.get('news_id')
    news_website_filter = args.get('news_website')
    category_filter = args.get('category')
    trend_filter = args.get('trend')
    limit = args.get('limit')
    if news_id_filter is not None:
        news_id_filter = int(re.sub(r'\D', "", news_id_filter))
        result = result.filter(News.news_id == news_id_filter)
    if news_website_filter is not None:
        result = result.filter(News.news_website == news_website_filter)
    if category_filter is not None:
        category_filter = int(re.sub(r'\D', "", category_filter))
        result = result.filter(News.category_id == category_filter)
    if trend_filter is not None:
        trend_filter = int(re.sub(r'\D', "", trend_filter))
        result = result.filter(News.trend_id == trend_filter)
    if limit is not None:
        limit = int(re.sub(r'\D', "", limit))
        result = result.limit(limit)

    output = NewsSchema(many=True).dump(result.all())
    return {'news': output}


def create():
    return {'news': "create"}


def update():
    return {'news': "update"}
