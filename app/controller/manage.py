from app import app
from flask import jsonify, request
from app.model.News import News, NewsSchema
from app.controller import fun, news, classifyChatbot
from flask_cors import CORS

app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, support_credentials=True)


@app.route('/')
def index():
    result = News.query.limit(5).all()
    output = NewsSchema(many=True).dump(result)
    return jsonify({'news': output}), 200


@app.route('/newslist', methods=['GET', 'POST', 'PUT'])
def newslist():
    if request.method == 'GET':
        output, status = news.read(news_id_filter=request.args.get('news_id'),
                                   news_website_filter=request.args.get('news_website'),
                                   category_filter=request.args.get('category'),
                                   trend_filter=request.args.get('trend'),
                                   datetime_filter=request.args.get('datetime'),
                                   limit=request.args.get('limit'))
        return jsonify(output), status

    elif request.method == 'POST':
        output, status = news.create(request.json["news"])
        return jsonify(output), status

    elif request.method == 'PUT':
        output, status = news.update(request.json["news"])
        return jsonify(output), status


@app.route("/chatbot", methods=['POST'])
def chatbot():
    context = str(request.json["context"])
    result = classifyChatbot.classifyChatbot(context)
    if "新聞" in result:
        output, status = fun.get_news(context)
        function = "news"
    elif "走勢" in result:
        output, status = fun.get_trend(context)
        function = "trend"
    elif "教學" in result:
        output, status = fun.get_tutorial(context)
        function = "tutorial"
    elif "市值" in result:
        output, status = fun.get_price(context)
        function = "price"
    else:
        output, status = fun.gSearch(context)
        function = "gSearch"
    result = jsonify({"function": function, "data": output, "errors": ""})
    return result, status
