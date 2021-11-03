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
        return jsonify({"function": "getNews", "data": output, "errors": ""}), status

    elif request.method == 'POST':
        output, status = news.create(request.json["news"])
        return jsonify({"function": "postNews", "data": output, "errors": ""}), status

    elif request.method == 'PUT':
        output, status = news.update(request.json["news"])
        return jsonify({"function": "putNews", "data": output, "errors": ""}), status


@app.route("/chatbot", methods=['POST'])
def chatbot():
    context = str(request.json["context"])
    result = classifyChatbot.classifyChatbot(context)
    if "新聞" in result:
        output, function, status = fun.get_news(context)
        return jsonify({"function": function, "data": output, "errors": ""}), status
    elif "走勢" in result:
        output, function, status = fun.get_trend(context)
        return send_file(output, mimetype='image/jpeg'), status
    elif "教學" in result:
        output, function, status = fun.get_tutorial(context)
        return jsonify({"function": function, "data": output, "errors": ""}), status
    elif "成交量" in result:
        output, function, status = fun.get_price(context)
        return jsonify({"function": function, "data": output, "errors": ""}), status
    else:
        output, function, status = fun.gSearch(context)
        return jsonify({"function": function, "data": output, "errors": ""}), status
