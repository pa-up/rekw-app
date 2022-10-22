def rekw_function(main_kw):
    # pip install 
    from selenium import webdriver    # webdriverをインポート
    from selenium.webdriver.common.by import By  # 要素を取得
    import pandas as pd
    from pandas import DataFrame    # DataFrame型の配列
    import numpy as np

    # ==============================================================
    # データを格納するリストと配列を定義
    # ==============================================================
    # 再検索kwを格納する配列を定義
    Re_kw_array  = np.empty( (8) , dtype = 'object' )        # 最初の階層のkwを格納
    Re_kw_array1 = np.empty( (8) , dtype = 'object' )        # 次の階層のkwを格納
    Re_kw_array2 = np.empty( (8) , dtype = 'object' )        # 次の階層のkwを格納
    Re_kw_array3 = np.empty( (8) , dtype = 'object' )        # 次の階層のkwを格納
    Re_kw_array4 = np.empty( (8) , dtype = 'object' )        # 次の階層のkwを格納
    Re_kw_array5 = np.empty( (8) , dtype = 'object' )        # 次の階層のkwを格納
    Re_kw_array6 = np.empty( (8) , dtype = 'object' )        # 次の階層のkwを格納
    Re_kw_array7 = np.empty( (8) , dtype = 'object' )        # 次の階層のkwを格納
    Re_kw_array8 = np.empty( (8) , dtype = 'object' )        # 次の階層のkwを格納
    

    # ==============================================================
    # クロムを起動
    # ==============================================================
    #Heroku内にあるChromedriverのパスを指定する
    driver = webdriver.Chrome('/app/.chromedriver/bin/chromedriver')


    # ==============================================================
    # 最初の階層スタート  (8つの再検索kwとそれぞれの階層へ遷移するためのURLも取得)
    # ==============================================================
    # Googleのブラウザを開く
    driver.get('https://www.google.com/')

    # 「メインkw」を検索
    search_box = driver.find_element(By.NAME, "q")   # 検索窓ページへアクセス
    search_box.send_keys(main_kw)    # 検索窓にメインkwを入力
    search_box.submit()

    # 最初の階層における、再検索kwのデータのグループを取得
    g_ary = driver.find_elements(By.CLASS_NAME, 'k8XOCe')
    # class「y6Uyqe」の中で、
    # # 「b」タグは再検索kwのテキストのみ、[a href]は再検索kwの検索結果画面のみ

    Re_kw_list = []  # リストを定義
    for g in g_ary:
        Re_kw = {}  # 辞書を定義
        
        # 各々の再検索kwのタイトル
        Re_kw['title'] = g.find_element(By.CLASS_NAME, 's75CSd').text
        Re_kw_list.append(Re_kw)
        
        # 処理内容 ： 新たに作った、リスト「Re_kw」に配列「Re_kw_array」に格納する
        for row, Re_kw in enumerate(Re_kw_list, 0):
            Re_kw_array[row] = Re_kw['title']
        #
    #

    # 現時点で、最初の階層での再検索kwを8つ取得
    # 次はアクセスリンクへ飛ぶ


    # ==============================================================
    # 2階層目スタート  （最初の階層の8つの再検索kwそれぞれで2階層目の再検索kwを取得）
    # ==============================================================
    for k in range(0, 8, 1):  # 再検索kwの数だけループ
        # 再度、Googleのブラウザを開く
        driver.get('https://www.google.com/')
        # 検索ボックスから、再検索kwを検索
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(Re_kw_array[k])   # 再検索kwを代入
        search_box.submit()
        
        # 再検索kwのデータのグループを取得
        g_ary2 = driver.find_elements(By.CLASS_NAME, 'k8XOCe') 
        Re_kw_list1 = []  # リストを定義
        Re_kw_list2 = []  # リストを定義
        Re_kw_list3 = []  # リストを定義
        Re_kw_list4 = []  # リストを定義
        Re_kw_list5 = []  # リストを定義
        Re_kw_list6 = []  # リストを定義
        Re_kw_list7 = []  # リストを定義
        Re_kw_list8 = []  # リストを定義

        for g in g_ary2:
            Re_kw = {}  # 辞書を定義
            # 各々の再検索kwのみを取得
            Re_kw['title'] = g.find_element(By.CLASS_NAME, 's75CSd').text

            if (k == 0):
                Re_kw_list1.append(Re_kw)
                for row, Re_kw in enumerate(Re_kw_list1, 0):
                    Re_kw_array1[row] = Re_kw['title']
                #
            #
            if (k == 1):
                Re_kw_list2.append(Re_kw)
                for row, Re_kw in enumerate(Re_kw_list2, 0):
                    Re_kw_array2[row] = Re_kw['title']
                #
            #
            if (k == 2):
                 Re_kw_list3.append(Re_kw)
                 for row, Re_kw in enumerate(Re_kw_list3, 0):
                    Re_kw_array3[row] = Re_kw['title']
                #
            #
            if (k == 3):
                Re_kw_list4.append(Re_kw)
                for row, Re_kw in enumerate(Re_kw_list4, 0):
                    Re_kw_array4[row] = Re_kw['title']
                #
            #
            if (k == 4):
                Re_kw_list5.append(Re_kw)
                for row, Re_kw in enumerate(Re_kw_list5, 0):
                    Re_kw_array5[row] = Re_kw['title']
                #
            #
            if (k == 5):
                Re_kw_list6.append(Re_kw)
                for row, Re_kw in enumerate(Re_kw_list6, 0):
                    Re_kw_array6[row] = Re_kw['title']
                #
            #
            if (k == 6):
                Re_kw_list7.append(Re_kw)
                for row, Re_kw in enumerate(Re_kw_list7, 0):
                    Re_kw_array7[row] = Re_kw['title']
                #
            #
            if (k == 7):
                Re_kw_list8.append(Re_kw)
                for row, Re_kw in enumerate(Re_kw_list8, 0):
                    Re_kw_array8[row] = Re_kw['title']
                #
            #
        # 8つの再検索kwそれぞれの階層でループ
    # 8つの再検索kwを全て取得済み

    # ==============================================================
    # 取得した再検索kwを Numpy配列に変換
    # ==============================================================
    # データフレームを定義

    # 「列名」  -> {検索kw}、 {1階層目の再検索kw}、{2階層目の再検索kw}
    columnsArray = np.empty( (3) , dtype = 'object' )
    columnsArray[0] = "検索kw"
    columnsArray[1] = "1階層目の再検索kw"
    columnsArray[2] = "2階層目の再検索kw"

    # 「値」  -> 50行2列
    valuesArray = np.empty((64,  3), dtype='object')

    for k2 in range(0, 3, 1):  # 列方向
        for k1 in range(0, 64, 1):  # 行方向

            # 検索kw
            if (k2 == 0):
                if (k1 == 0):
                    valuesArray[0][0] = main_kw
                #
                if (k1 != 0):
                    valuesArray[k1][k2] = ""
                #
            #

            # 1階層目の再建策kw
            if (k2 == 1):
                if (k1 <= 7):
                    if (k1 == 0):
                        valuesArray[k1][k2] = Re_kw_array[0]
                    #
                    if (k1 != 0):
                        valuesArray[k1][k2] = ""
                    #
                #
                if (k1 <= 15 and k1 > 7):
                    if (k1 == 8):
                        valuesArray[k1][k2] = Re_kw_array[1]
                    #
                    if (k1 != 8):
                        valuesArray[k1][k2] = ""
                    #
                #
                if (k1 <= 23 and k1 > 15):
                    if (k1 == 16):
                        valuesArray[k1][k2] = Re_kw_array[2]
                    #
                    if (k1 != 16):
                        valuesArray[k1][k2] = ""
                    #
                #
                if (k1 <= 31 and k1 > 23):
                    if (k1 == 24):
                        valuesArray[k1][k2] = Re_kw_array[3]
                    #
                    if (k1 != 24):
                        valuesArray[k1][k2] = ""
                    #
                #
                if (k1 <= 39 and k1 > 31):
                    if (k1 == 32):
                        valuesArray[k1][k2] = Re_kw_array[4]
                    #
                    if (k1 != 32):
                        valuesArray[k1][k2] = ""
                    #
                #
                if (k1 <= 47 and k1 > 39):
                    if (k1 == 40):
                        valuesArray[k1][k2] = Re_kw_array[5]
                    #
                    if (k1 != 40):
                        valuesArray[k1][k2] = ""
                    #
                #
                if (k1 <= 55 and k1 > 47):
                    if (k1 == 48):
                        valuesArray[k1][k2] = Re_kw_array[6]
                    #
                    if (k1 != 48):
                        valuesArray[k1][k2] = ""
                    #
                #
                if (k1 <= 63 and k1 > 55):
                    if (k1 == 56):
                        valuesArray[k1][k2] = Re_kw_array[7]
                    #
                    if (k1 != 56):
                        valuesArray[k1][k2] = ""
                    #
                #
            #
            
            # 2階層目の再検索kw
            if (k2 == 2):
                if (k1 <= 7):
                    valuesArray[k1][k2] = Re_kw_array1[k1]
                #
                if (k1 <= 15 and k1 > 7):
                    valuesArray[k1][k2] = Re_kw_array2[k1-8]
                #
                if (k1 <= 23 and k1 > 15):
                    valuesArray[k1][k2] = Re_kw_array3[k1-16]
                #
                if (k1 <= 31 and k1 > 23):
                    valuesArray[k1][k2] = Re_kw_array4[k1-24]
                #
                if (k1 <= 39 and k1 > 31):
                    valuesArray[k1][k2] = Re_kw_array5[k1-32]
                #
                if (k1 <= 47 and k1 > 39):
                    valuesArray[k1][k2] = Re_kw_array6[k1-40]
                #
                if (k1 <= 55 and k1 > 47):
                    valuesArray[k1][k2] = Re_kw_array7[k1-48]
                #
                if (k1 <= 63 and k1 > 55):
                    valuesArray[k1][k2] = Re_kw_array8[k1-56]
                #
            #
        #
    #

    # ==============================================================
    # numpy配列をCSVに保存
    # ==============================================================
    #csv_data = DataFrame(valuesArray, columns = columnsArray, index=False)


    # ==============================================================
    # numpy配列をリストに変換
    # ==============================================================
    col_list = [ columnsArray[0] , columnsArray[1] , columnsArray[2] ]

    val_list = [ [0]*3 for i in range(64) ]
    for k1 in range(0, 64, 1):
        for k2 in range(0, 3, 1):
            val_list[k1][k2] = valuesArray[k1][k2]
        #
    #


    # ==============================================================
    # 「main.py」に再検索キーワードのhtmlデータを返り値として、送信
    # ==============================================================
    return col_list, val_list
#
    
    












