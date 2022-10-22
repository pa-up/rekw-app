# アプリ名：rekw-app

#========================================================
# 最初に必要なインポート
#========================================================
import os
from flask import Flask,request,render_template
app = Flask(__name__)

#「rekw_algorithm.py」からのインポート
import rekw_get


#========================================================
# 検索窓のページを表示
#========================================================
@app.route("/search")   #「/search」のサイトで関数「show()」を実行
def show():
    return render_template("search.html")
#


#========================================================
# 再検索キーワードの出力ページを表示
#========================================================
# 検索窓ページで取得したメインキーワード
main_kw = request.form["article"]

@app.route("/result",methods=["POST"])   #「/result」のサイトで関数「result()」を実行
def result():

    # 「rekw_get.py」から返り値「html_data」をこちらのファイルにインポート
    reKw_data, csv_data = rekw_get.rekw_function(main_kw)

    # フォルダ「rekw_save」内にCSVファイルがあれば、削除
    file_exsit = os.path.isfile("./rekw_save/rekw.csv")
    if file_exsit == True:
        os.remove("./rekw_save/rekw.csv")
    #

    # フォルダ「rekw_save」にCSVファイルを生成
    csv_data.to_csv("rekw_save\\rekw.csv", index=False)

    # 再検索キーワードの出力結果ページ
    return render_template("result.html" , reKw_data=reKw_data ,  main_kw=main_kw)
#

