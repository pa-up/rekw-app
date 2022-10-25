# アプリ名：rekw-app

#========================================================
# 最初に必要なインポート
#========================================================
from pandas import DataFrame    # DataFrame型の配列
import os
import csv
from flask import Flask, request, render_template, session

app = Flask(__name__)
app.secret_key = 'csv_data_save'

#「rekw_algorithm.py」からのインポート
import rekw_get


#========================================================
# 検索窓のページを表示
#========================================================
@app.route("/")   #「/search」のサイトで関数「show()」を実行
def show():
    return render_template("search.html")
#


#========================================================
# 再検索キーワードの出力ページを表示
#========================================================
# 検索窓ページで取得したメインキーワード
@app.route("/result",methods=["POST"])   #「/result」のサイトで関数「result()」を実行
def result():
    main_kw = request.form["article"]

    # 「rekw_get.py」から返り値「html_data」をこちらのファイルにインポート
    col_list, val_list = rekw_get.rekw_function(main_kw)
    
    # csv.htmlで使うデータ
    session["csv_col"] = col_list
    session["csv_val"] = val_list

    # 再検索キーワードの出力結果ページ
    return render_template("result.html", col_list=col_list , val_list=val_list)
#


#========================================================
# CSVデータの取得
#========================================================
# CSVを保存するためだけのページ（heroku無料版だとこれが限界？）
@app.route("/csv", methods=["POST"])  # 「/csv」のサイトで関数「csv()」を実行
def csv():
    col_list = session["csv_col"]
    val_list = session["csv_val"]

    csv_data = DataFrame(val_list, columns=col_list)

    # フォルダ「rekw_save」にCSVファイルを生成
    csv_data.to_csv("/data/csv/rekw.csv", index=False)

    # 再検索キーワードの出力結果ページ
    return render_template("csv.html", csv_data=csv_data)
#
