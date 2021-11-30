from sqlalchemy import desc
from app.model.News import News, NewsSchema
from app import db
import re


def read(news_id_filter=None, news_website_filter=None, category_filter=None, trend_filter=None, datetime_filter=None, limit=None):
    result = News.query.order_by(desc('news_datetime'))
    if news_id_filter is not None:
        news_id_filter = int(re.sub(r'\D', "", news_id_filter))
        result = result.filter(News.news_id == news_id_filter)
    if news_website_filter is not None:
        result = result.filter(News.news_website == news_website_filter)
    if category_filter is not None:
        category_filter = None if category_filter == 'NULL' else int(re.sub(r'\D', "", category_filter))
        result = result.filter(News.category_id == category_filter)
    if trend_filter is not None:
        trend_filter = None if trend_filter == 'NULL' else int(re.sub(r'\D', "", trend_filter))
        result = result.filter(News.trend_id == trend_filter)
    if datetime_filter is not None:
        result = result.filter(News.news_datetime >= datetime_filter)
    if limit is not None:
        limit = int(re.sub(r'\D', "", limit))
        result = result.limit(limit)
    output = NewsSchema(many=True).dump(result.all())
    return {'news': output}, "getNews", 200


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
        create_news = News(news_datetime=news_datetime, news_title=news_title, news_content=news_content,
                           news_website=news_website, news_link=news_link, img_link=img_link, category_id=category_id, trend_id=trend_id)
        db.session.add(create_news)
    db.session.commit()
    return {'result': 'create success'}, "postNews", 200


def update(args):
    if len([news for news in args if (news.get('news_id') is None)|(news.get('news_datetime') is None)]): 
        return 'news_id & datetime is required', "putNews", 400
    
    # sort array by key = 'news_datetime'
    args = sorted(args, key=lambda k: k['news_datetime'], reverse=False)

    # get query
    oriNews_list = News.query.filter(News.news_datetime >= args[0]['news_datetime']).order_by(desc('news_datetime')).all()
    
    # loop by new array
    for n in args:
        new_category = n.get('category_id')
        new_trend = n.get('trend_id')

        # find ori.news_id == n.news_id
        news = [ori for ori in oriNews_list if ori.news_id == n.get('news_id')][0]
        if new_category is not None:
            news.category_id = new_category
        if new_trend is not None:
            news.trend_id = new_trend

        db.session.add(news)
    db.session.commit()
    return {'result': 'update success'}, "putNews", 200