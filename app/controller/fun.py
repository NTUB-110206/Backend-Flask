import os
import requests
from datetime import date, timedelta
from app.controller import news


def get_news(context):
    # 今天 昨天 正面 負面
    dayFilter = dayFilterLogic(context)
    trend = None
    if "正面" in context:
        trend = "1"
    elif "負面" in context:
        trend = "0"

    if dayFilter == "unknown":
        output, status = gSearch(context)
        function = "gSearch"
    else:
        output, status = news.read(trend_filter=trend, datetime_filter=dayFilter)
        function = "getNews"

    return output, function, status


def get_trend(context):
    dayFilter = dayFilterLogic(context)
    return "走勢", "getTrend", 200


def get_tutorial(context):
    # template
    return "教學", "getTutorial", 200


def get_price(context):
    # 成交量 比特幣（個）＊單價
    dayFilter = dayFilterLogic(context)
    return "成交量", "getPrice", 200


def gSearch(context):
    cx = os.getenv('GSEARCH_CX')
    key = os.getenv('GSEARCH_KEY')

    if len(cx) and len(key):
        my_params = {'cx': cx, 'key': key, 'q': context}
        res = requests.get('https://www.googleapis.com/customsearch/v1', params=my_params)
        results = res.json()
        return results['items'], "gSearch", 200
    else:
        return "gSearch cannot use", "gSearch", 200


def dayFilterLogic(context):

    if "今天" in context:
        dayFilter = date.today()
    elif "昨天" in context:
        dayFilter = date.today() - timedelta(days=1)
    elif "本週" in context:
        dayFilter = date.today() - timedelta(weeks=7)
    elif "本月" in context:
        dayFilter = date.today() - timedelta(days=30)
    elif "今年" in context:
        dayFilter = date.today() - timedelta(days=365)
    else:
        dayFilter = "unknown"

    return dayFilter
