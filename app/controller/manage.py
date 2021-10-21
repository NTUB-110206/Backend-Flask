from app import app
from flask import jsonify, request
from app.model.News import News, NewsSchema
from app.controller import fun, news, nlp
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
        output, status = news.read(request.args)
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
    result = nlp.nlp(context)
    if "新聞" in result:
        reply = fun.news()
        function = "news"
    elif "走勢" in result:
        reply = fun.trend()
        function = "trend"
    elif "教學" in result:
        reply = fun.tutorial()
        function = "tutorial"
    elif "市值" in result:
        reply = fun.price()
        function = "price"
    else:
        reply = fun.gSearch(context)
        function = "gSearch"
    result = jsonify({"function": function, "data": reply, "errors": ""})
    return result, 200
