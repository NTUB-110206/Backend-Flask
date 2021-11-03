import requests


def get_gSeacrh_data(cx, key, context):
    my_params = {'cx': cx, 'key': key, 'q': context}
    res = requests.get('https://www.googleapis.com/customsearch/v1', params=my_params)
    results = res.json()
    return results


