import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import joblib
def nlp(context):
    # # 使用Python pandas套件讀取檔案
    read = pd.read_excel("data/traindata.xlsx", index_col=False).values.tolist()

    corpus = [row[0] for row in read]
    intents = [row[1] for row in read]
    # 印出來看看是否成功
    # print(corpus[:15])

    # 向量化
    feature_extractor = CountVectorizer(analyzer="word", ngram_range=(1, 2), binary=True, token_pattern=r'([a-zA-Z]+|\w)')
    X = feature_extractor.fit_transform(corpus)
    # 總共得到多少數量的特徵
    # print(len(feature_extractor.get_feature_names_out()))
    # 得到的特徵前三十筆
    # print(feature_extractor.get_feature_names_out()[:30])

    # 分類
    INTENT_CLASSIFY_REGULARIZATION = "l2"
    lr = LogisticRegression(penalty=INTENT_CLASSIFY_REGULARIZATION, class_weight='balanced')
    lr.fit(X, intents)

    # 預測
    user_input = [context]
    X2 = feature_extractor.transform(user_input)
    # print(len(X2.toarray()[0]))
    # print(X2)

    # feature_names = feature_extractor.get_feature_names_out()
    # for index in X2.nonzero()[1]:
    #     print(feature_names[index])

    lr.predict(X2)
    probs = lr.predict_proba(X2)[0]
    # for predict_intent, prob in sorted(zip(lr.classes_, probs), key = lambda x: x[1],reverse = True):
    #     print(predict_intent, prob)

    predict = (sorted(zip(lr.classes_, probs), key = lambda x: x[1],reverse = True)[0])
    result = predict[0]
    prob = predict[1]
    if prob < 0.1 : result = "unknown"
    
    return result