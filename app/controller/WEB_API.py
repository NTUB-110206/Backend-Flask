import requests


def get_gSeacrh_data(cx, key, context):
    my_params = {'cx': cx, 'key': key, 'q': context}
    res = requests.get('https://www.googleapis.com/customsearch/v1', params=my_params)
    results = res.json()
    return results


def get_crypto_data(from_sym='BTC', to_sym='USD', timeframe='day', limit=2000, aggregation=1):
    parameters = {
        'fsym': from_sym,
        'tsym': to_sym,
        'limit': limit,
        'aggregate': aggregation
    }
    res = requests.get('https://min-api.cryptocompare.com/data/v2/histo'+timeframe, params=parameters)
    data = res.json()
    print(data)
    return data['Data']['Data']
