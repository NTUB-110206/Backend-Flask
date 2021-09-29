from app import app
from flask import jsonify, request
from app.model.News import News, NewsSchema
from app.controller import fun
from flask_cors import CORS

app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, support_credentials=True)


@app.route('/')
def index():
    result = News.query.limit(5).all()
    output = NewsSchema(many=True).dump(result)
    return jsonify({'news':output}), 200


@app.route("/chatbot", methods=['POST'])
def chatbot():
    context = str(request.json["context"])
    print(context)
    reply = ""
    if "新聞" in context:
        reply = fun.news()
    elif "走勢" in context:
        reply = fun.trend()
    elif "懶人包" in context:
        reply = fun.tutorial()
    elif "市值" in context:
        reply = fun.price()

    result = jsonify({"data": reply, "errors": ""})
    return result, 200
