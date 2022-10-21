from flask import Flask,request,render_template
app = Flask(__name__)


@app.route("/")
def show():
    return render_template("index.html")


# 「request」をインポートにより、html側でフォームに入力したデータを取り出せる
@app.route("/result",methods=["POST"])
def result():
    article = request.form["article"]
    name = request.form["name"]
    return render_template("index.html",article=article,name=name)