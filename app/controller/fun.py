import os
from app.controller import news, WEB_API, utils


def get_news(context):
    # 今天 昨天 正面 負面
    dayFilter = utils.dayFilterLogic(context)
    trend = None
    if any(txt in context for txt in ['正面', '正向', '正', '看多', '政', '鄭', '證', '証']):
        trend = "1"
    elif any(txt in context for txt in ['負面', '負向', '負', '看空', '副','富', '付', '復']):
        trend = "0"

    if dayFilter == "unknown":
        output, function, status = gSearch(context)
    else:
        output, function, status = news.read(trend_filter=trend, datetime_filter=dayFilter)
        function = "getNews"

    return output, function, status


def get_trend(context):
    dayFilter = utils.dayFilterLogic(context)
    print('y' if any(txt in context for txt in ['預測', '預', '預估', '未來', '明天', '下']) else 'n')
    if any(txt in context for txt in ['預測', '預', '預估', '未來', '明天', '下']):
        result = WEB_API.get_ClosedPricePic_Predict()
        output, function = {'img_url': result['result'], 'width': 1400, 'height': 1000}, "getTrend"
    elif dayFilter == "unknown":
        output, function, status = gSearch(context)
    else:
        limitday = utils.get_date(dayFilter)
        data = WEB_API.get_crypto_data(limit=(1 if limitday==0 else limitday))
        img_path = utils.plot_data(utils.data_to_dataframe(data), days=dayFilter)
        imgur_result = WEB_API.imgur_upload(img_path)
        output, function = {'img_url': imgur_result['link'], 'width': imgur_result['width'], 'height': imgur_result['height']}, "getTrend"
    
    return output, function, 200


def get_tutorial(context):
    # template
    return "教學", "getTutorial", 200


def get_price(context):
    # 成交量 比特幣（個）＊單價
    dayFilter = utils.dayFilterLogic(context)
    if any("context" in s for s in ['預測', '預', '預估', '未來', '明天', '下']):
        print('tomorrowgetPrice')
        output = WEB_API.get_ClosedPrice_Predict()['result']
        function = "getPrice"
    elif dayFilter == "unknown":
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

