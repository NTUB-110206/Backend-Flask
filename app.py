from flask import Flask
from flask import request
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
        reply = "新聞"
    elif "走勢" in context:
        reply = "走勢"
    elif "懶人包" in context:
        reply = "懶人包"
    elif "市值" in context:
        reply = "市值"
    return reply


app.run()
