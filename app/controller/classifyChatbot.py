import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import joblib


def classifyChatbot(context):
    # # 使用Python pandas套件讀取檔案
    read = pd.read_excel("data/classifyChatbot.xlsx", index_col=False).values.tolist()
    corpus = [row[0] for row in read]

    # 向量化
    feature_extractor = CountVectorizer(analyzer="word", ngram_range=(1, 2), binary=True, token_pattern=r'([a-zA-Z]+|\w)')
    X = feature_extractor.fit_transform(corpus)

    loaded_model = joblib.load('data/LR_model')

    # 預測
    user_input = [context]
    X2 = feature_extractor.transform(user_input)

    loaded_model.predict(X2)
    probs = loaded_model.predict_proba(X2)[0]

    predict = (sorted(zip(loaded_model.classes_, probs), key=lambda x: x[1], reverse=True)[0])
    result = predict[0]
    prob = predict[1]
    print(predict)
    if prob < 0.3:
        result = "unknown"

    return result
