import os
from app.controller import news, WEB_API, utils


def get_news(context):
    # 今天 昨天 正面 負面
    dayFilter = utils.dayFilterLogic(context)
    trend = None
    if "正面" in context:
        trend = "1"
    elif "負面" in context:
        trend = "0"

    if dayFilter == "unknown":
        output, function, status = gSearch(context)
    else:
        output, function, status = news.read(trend_filter=trend, datetime_filter=dayFilter)
        function = "getNews"

    return output, function, status


def get_trend(context):
    dayFilter = utils.dayFilterLogic(context)
    if dayFilter == "unknown":
        output, function, status = gSearch(context)
    else:
        limitday = utils.get_date(dayFilter)
        data = WEB_API.get_crypto_data(limit=(1 if limitday==0 else limitday))
        utils.plot_data(utils.data_to_dataframe(data), days=dayFilter)
        function = "getTrend"
        output = "../data/trend.jpg"
    
    return output, function, 200


def get_tutorial(context):
    # template
    return "教學", "getTutorial", 200


def get_price(context):
    # 成交量 比特幣（個）＊單價
    dayFilter = utils.dayFilterLogic(context)
    if dayFilter == "unknown":
        output, function, status = gSearch(context)
    else:
        limitday = utils.get_date(dayFilter)
        if limitday==0:
            output = WEB_API.get_crypto_data(limit=1)[1]['close']
        else:
            output = WEB_API.get_crypto_data(limit=limitday)[0]['close']
        function = "getPrice"
    return output, function, 200


def gSearch(context):
    cx = os.getenv('GSEARCH_CX')
    key = os.getenv('GSEARCH_KEY')

    if len(cx) and len(key):
        results = WEB_API.get_gSeacrh_data(cx, key, context)
        return results['items'], "gSearch", 200
    else:
        return "gSearch cannot use", "gSearch", 200

