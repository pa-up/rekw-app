def rekw_function(main_kw):
    # pip install 
    from selenium import webdriver    # webdriverをインポート
    from selenium.webdriver.common.by import By  # 要素を取得
    import pandas as pd
    from pandas import DataFrame    # DataFrame型の配列
    import numpy as np

    # ==============================================================
    # 再検索kwデータを格納する配列を定義
    # ==============================================================
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

    # 現在の問題点： herokuに設定したChromのバージョンが古すぎる


    # ==============================================================
    # 最初の階層スタート  (8つの再検索kwとそれぞれの階層へ遷移するためのURLも取得)
    # ==============================================================
    # Googleのブラウザを開く
    driver.get('https://www.google.com/')

    #「メインkw」を検索
    search_box = driver.find_element(By.NAME, "q")   # 検索窓ページへアクセス
    search_box.send_keys(main_kw)    # 検索窓にメインkwを入力
    search_box.submit()

    # 最初の階層における、再検索kwのデータのグループを取得（リンクやテキストなどの情報が包括）
    g_ary = driver.find_elements(By.CLASS_NAME, 'k8XOCe')

    Re_kw_list = []  # リストを定義
    for g in g_ary:
        Re_kw = {}  # 辞書を定義
        
        # 各々の再検索kwのテキスト
        Re_kw['title'] = g.find_element(By.CLASS_NAME, 's75CSd').text
        Re_kw_list.append(Re_kw)
        
        # リスト「Re_kw」をNumpy配列「Re_kw_array」に格納する
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
        # リストを定義
        Re_kw_list1 = []  
        Re_kw_list2 = []
        Re_kw_list3 = []
        Re_kw_list4 = []
        Re_kw_list5 = []
        Re_kw_list6 = []
        Re_kw_list7 = []
        Re_kw_list8 = []

        for g in g_ary2:
            Re_kw = {}  # 辞書を定義
            # 各々の再検索kwのみを取得
            Re_kw['title'] = g.find_element(By.CLASS_NAME, 's75CSd').text


            # リスト「Re_kw」をNumpy配列「Re_kw_array」に格納する

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
    # Numpy配列を「見栄えの良いCSV」になるように、リストに格納
    # ==============================================================
    # データフレームを定義

    # 「列名」  -> {検索kw}、 {1階層目の再検索kw}、{2階層目の再検索kw}
    col_list = [ "検索したキーワード" , "1階層目の再検索キーワード" , "2階層目の再検索キーワード" ]

    
    # 「値」  -> 50行3列
    val_list = []

    for k2 in range(0, 3, 1):  # 列方向
        val_col_list = []

        for k1 in range(0, 64, 1):  # 行方向

            # 検索kw
            if (k2 == 0):
                if (k1 == 0):
                    val_col_list.append(main_kw)
                #
                if (k1 != 0):
                    val_col_list.append("")
                #
            #

            # 1階層目の再建策kw
            if (k2 == 1):
                if (k1 <= 7):
                    if (k1 == 0):
                        val_col_list.append( Re_kw_array[0])
                    #
                    if (k1 != 0):
                        val_col_list.append("")
                    #
                #
                if (k1 <= 15 and k1 > 7):
                    if (k1 == 8):
                        val_col_list.append( Re_kw_array[1])
                    #
                    if (k1 != 8):
                        val_col_list.append("")
                    #
                #
                if (k1 <= 23 and k1 > 15):
                    if (k1 == 16):
                        val_col_list.append( Re_kw_array[2])
                    #
                    if (k1 != 16):
                        val_col_list.append("")
                    #
                #
                if (k1 <= 31 and k1 > 23):
                    if (k1 == 24):
                        val_col_list.append( Re_kw_array[3])
                    #
                    if (k1 != 24):
                        val_col_list.append("")
                    #
                #
                if (k1 <= 39 and k1 > 31):
                    if (k1 == 32):
                        val_col_list.append( Re_kw_array[4])
                    #
                    if (k1 != 32):
                        val_col_list.append("")
                    #
                #
                if (k1 <= 47 and k1 > 39):
                    if (k1 == 40):
                        val_col_list.append( Re_kw_array[5])
                    #
                    if (k1 != 40):
                        val_col_list.append("")
                    #
                #
                if (k1 <= 55 and k1 > 47):
                    if (k1 == 48):
                        val_col_list.append( Re_kw_array[6])
                    #
                    if (k1 != 48):
                        val_col_list.append("")
                    #
                #
                if (k1 <= 63 and k1 > 55):
                    if (k1 == 56):
                        val_col_list.append( Re_kw_array[7])
                    #
                    if (k1 != 56):
                        val_col_list.append("")
                    #
                #
            #
            
            # 2階層目の再検索kw
            if (k2 == 2):
                if (k1 <= 7):
                    val_col_list.append(Re_kw_array1[k1])
                #
                if (k1 <= 15 and k1 > 7):
                    val_col_list.append(Re_kw_array2[k1-8])
                #
                if (k1 <= 23 and k1 > 15):
                    val_col_list.append(Re_kw_array3[k1-16])
                #
                if (k1 <= 31 and k1 > 23):
                    val_col_list.append(Re_kw_array4[k1-24])
                #
                if (k1 <= 39 and k1 > 31):
                    val_col_list.append(Re_kw_array5[k1-32])
                #
                if (k1 <= 47 and k1 > 39):
                    val_col_list.append(Re_kw_array6[k1-40])
                #
                if (k1 <= 55 and k1 > 47):
                    val_col_list.append(Re_kw_array7[k1-48])
                #
                if (k1 <= 63 and k1 > 55):
                    val_col_list.append(Re_kw_array8[k1-56])
                #
            #
        #
        val_list.append(val_col_list)
    #
    # リスト配列を転置
    val_list_t = list(zip(*val_list))

    # ==============================================================
    # numpy配列をCSVに保存
    # ==============================================================
    #csv_data = DataFrame(val_list_t, columns = col_list)


    # ==============================================================
    # 「main.py」に再検索キーワードのhtmlデータを返り値として、送信
    # ==============================================================
    return col_list, val_list_t
#
    
    












