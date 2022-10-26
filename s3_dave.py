#=====================================================================
# このファイルを実行する前に、
# 「main.py」の処理で保存したいファイルを一時的にHeroku Dynoに保存しておく
#=====================================================================
# 「main.py」でのコード記載例
# file_name = 'rekw.csv'    # ファイル名の決定
# csv_data.to_csv(file_name, index=False)    # CSVの一時的な生成
# s3_csv_url = s3_dave.csv_bots(file_name)    # このファイルの関数を実行
#=====================================================================

import boto3

def csv_boto3(file_name):
    
    # s3のユーザー情報を記載
    accesskey = "AKIAYDGH7WYNYWMOPDD2"
    secretkey = "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"
    region = "ap-northeast-1"   # 東京(アジアパシフィック)：ap-northeast-1
    bucket_name = "rekw-csv-save"

    # s3へcsvファイルをアップロード
    s3 = boto3.client('s3', aws_access_key_id=accesskey, aws_secret_access_key=secretkey, region_name=region)
    s3.upload_file(file_name, bucket_name, file_name)

    # S3へアップロードしたCSVへのURLを取得する
    s3_url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': bucket_name, 'Key': file_name},
        ExpiresIn=3600,
        HttpMethod='GET'
    )

    return s3_url
#