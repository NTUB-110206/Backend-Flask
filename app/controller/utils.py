from datetime import date, datetime, timedelta

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
        dayFilter = date.today() - timedelta(days=365)

    return dayFilter