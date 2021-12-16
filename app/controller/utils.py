from datetime import date, timedelta, datetime
from pandas.plotting import register_matplotlib_converters
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def get_date(inputday):
    delta = date.today() - inputday
    return int(delta.days)

def data_to_dataframe(data):

    df = pd.DataFrame.from_dict(data)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

def plot_data(df, cryptocurrency='BTC', target_currency='USD', days=2000):

    register_matplotlib_converters()
    plt.figure(figsize=(7,5))
    plt.title('{} / {} price data'.format(cryptocurrency, target_currency))
    plt.plot(df['time'], df['close'], label='BTC')
    plt.legend()
    plt.xticks(rotation=20)
    fig = plt.gcf()
    img_path = './data/'+datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')+'-trend.jpg'
    fig.savefig(img_path, dpi=200)
    return img_path


def dayFilterLogic(context):
    Today_list = ['今天', '今日', '現在', '本日', '最新', '最近']
    Yesterday_list = ['昨天', '昨日', '作天', '昨', '近兩天']
    ThisWeek_list = ['本週', '本周', '這周', '本周','這個禮拜', '這禮拜']
    ThisMonth_list = ['本月', '這個月']
    ThisYear_list = ['今年', '本年', '這一年']
    if any(txt in context for txt in Today_list):
        dayFilter = date.today()
    elif any(txt in context for txt in Yesterday_list):
        dayFilter = date.today() - timedelta(days=1)
    elif any(txt in context for txt in ThisWeek_list):
        dayFilter = date.today() - timedelta(weeks=7)
    elif any(txt in context for txt in ThisMonth_list):
        dayFilter = date.today() - timedelta(days=30)
    elif any(txt in context for txt in ThisYear_list):
        dayFilter = date.today() - timedelta(days=365)
    else:
        dayFilter = "unknown"
    print(dayFilter)
    return dayFilter