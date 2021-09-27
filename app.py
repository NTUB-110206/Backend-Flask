from flask import Flask
from flask import request
from flask import jsonify

import fun

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Flask"


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


app.run()