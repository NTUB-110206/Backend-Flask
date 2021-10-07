from sqlalchemy import desc
from app.model.News import News, NewsSchema
from app import db
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


def create(args):
    for n in args:
        news_datetime = n.get('news_datetime')
        news_title = n.get('news_title')
        news_content = n.get('news_content')
        news_website = n.get('news_website')
        news_link = n.get('news_link')
        img_link = n.get('img_link')
        category_id = n.get('category_id')
        trend_id = n.get('trend_id')
        create_news = News(news_datetime=news_datetime, news_title=news_title, news_content=news_content, news_website=news_website, news_link=news_link, img_link=img_link, category_id=category_id, trend_id=trend_id)
        db.session.add(create_news)
    db.session.commit()
    return {'result': 'create success'}


def update():
    return {'news': "update"}
