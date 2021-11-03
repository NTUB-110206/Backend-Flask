from app import app
from flask import jsonify, request, send_file
from app.model.News import News, NewsSchema
from app.controller import fun, news, classifyChatbot
from flask_cors import CORS

app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, support_credentials=True)


@app.route('/')
def index():
    result = News.query.limit(5).all()
    output = NewsSchema(many=True).dump(result)
    return jsonify({'news': output}), 200, {"function": "getNews"}


@app.route('/newslist', methods=['GET', 'POST', 'PUT'])
def newslist():
    if request.method == 'GET':
        output, function, status = news.read(news_id_filter=request.args.get('news_id'),
                                   news_website_filter=request.args.get('news_website'),
                                   category_filter=request.args.get('category'),
                                   trend_filter=request.args.get('trend'),
                                   datetime_filter=request.args.get('datetime'),
                                   limit=request.args.get('limit'))

    elif request.method == 'POST':
        output, function, status = news.create(request.json["news"])

    elif request.method == 'PUT':
        output, function, status = news.update(request.json["news"])
        
    return jsonify({"data": output}), status, {"function": function}


@app.route("/chatbot", methods=['GET'])
def chatbot():
    context = request.args.get("context")
    result = classifyChatbot.classifyChatbot(context)
    if "新聞" in result:
        output, function, status = fun.get_news(context)
        response = jsonify({"data": output})
    elif "走勢" in result:
        output, function, status = fun.get_trend(context)
        response = send_file(output, mimetype='image/jpeg') if function == "getTrend" else jsonify({"data": output})
    elif "教學" in result:
        output, function, status = fun.get_tutorial(context)
        response = jsonify({"data": output})
    elif "成交量" in result:
        output, function, status = fun.get_price(context)
        response = jsonify({"data": output})
    else:
        output, function, status = fun.gSearch(context)
        response = jsonify({"data": output})
    return response, status, {"function": function}
