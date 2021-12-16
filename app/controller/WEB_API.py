import os
import requests  
from imgurpython import ImgurClient

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


def imgur_upload(img_path):
    client_data = ImgurClient(os.getenv('client_id'), os.getenv('client_secret'), os.getenv('access_token'), os.getenv('refresh_token'))
    image_url = client_data.upload_from_path(img_path, config=None, anon=False)
    return image_url

def get_ClosedPricePic_Predict():
    res = requests.get(os.getenv('NLPService')+'/ClosedPricePic_Predict')
    results = res.json()
    return results
def get_ClosedPrice_Predict():
    res = requests.get(os.getenv('NLPService')+'/ClosedPrice_Predict')
    results = res.json()
    return results