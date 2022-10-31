# アプリ名：rekw-app

#========================================================
# 最初に必要なインポート
#========================================================
from pandas import DataFrame    # DataFrame型の配列
import cv2
from flask import Flask, request, render_template, session

app = Flask(__name__)
app.secret_key = 'csv_data_save'

#他のPythonファイルからのインポート
import rekw_get
import s3_dave


#========================================================
# 検索窓のページを表示
#========================================================
@app.route("/")   #「/search」のサイトで関数「show()」を実行
def show():
    # 画像ファイルを一時的にHeroku Dynoに保存
    file_name = 'rekw_img.png'
    file_path = "./data/img/rekw_img.png"
    file_data = cv2.imread(file_path)
    cv2.imwrite(file_name, file_data)

    # 「s3_save.py」を実行して、s3にアップロードされたCSVへのURLを取得
    s3_img_url = s3_dave.file_boto3(file_name)
    return render_template("search.html", s3_img_url=s3_img_url)
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
    
    # CSVデータフレームを生成
    csv_data = DataFrame(val_list, columns=col_list)

    # CSVファイルを生成し、一時的にHeroku Dynoに保存
    file_name = 'rekw.csv'
    csv_data.to_csv(file_name,encoding='shift_jis')

    # 「s3_save.py」を実行して、s3にアップロードされたCSVへのURLを取得
    s3_csv_url = s3_dave.file_boto3(file_name)

    # 再検索キーワードの出力結果ページ
    return render_template("result.html", col_list=col_list , val_list=val_list, s3_csv_url=s3_csv_url)
#