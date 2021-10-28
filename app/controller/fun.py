import os
import requests
from datetime import date, timedelta

def news():
    return "新聞"

def trend():
    return "走勢"

def tutorial():
    return "懶人包"

def price():
    return "市值"

def gSearch(context):
    cx = os.getenv('GSEARCH_CX')
    key = os.getenv('GSEARCH_KEY')

    if len(cx) and len(key):
        my_params = {'cx': cx, 'key': key, 'q': context}
        res = requests.get('https://www.googleapis.com/customsearch/v1', params=my_params)
        results = res.json()
        return results['items']
    else:
        return "gSearch cannot use"

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
