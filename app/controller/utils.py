from datetime import date, timedelta
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
    plt.xticks(rotation=45)
    fig = plt.gcf()
    fig.savefig('./data/trend.jpg', dpi=200)
    return plt


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