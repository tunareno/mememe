from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>池偉銘網頁</h1>"
    homepage += "<a href=/me>偉銘簡介網頁</a><br>"
    homepage += "<a href=/mis>MIS工作介紹</a><br>"
    homepage += "<a href=/today>職涯測驗結果</a><br>"
    homepage += "<a href=/welcome?nick=tcyang>求職履歷</a><br>"
    return homepage

@app.route("/mis")
def course():
    return render_template("MIS.html")


@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/me")
def me():
    return render_template("aboutme.html")