import numpy as np
import csv
import sys
import os, fnmatch

#データファイルの読み込み(相対パスで指定すれば任意のディレクトリの中のファイルも読み込める)
print("入力ファイル名を拡張子も含めて入力してください．ディレクトリ内のtxtファイル全てについて行う場合は\"ALL\"と入力してください．")
inputfile = input()

#全てのファイルの場合
if inputfile == 'ALL':
    #指定したディレクトリのファイルを全て取得する
    files = os.listdir('.')
    #全てのファイルから拡張子がtxtのファイルだけを抜き出す
    txts = fnmatch.filter(files, '*.txt')
    #txtファイル全てに対してCSV変換を施す
    for txt in txts:
        #whitespaceをdelimiterに持つデータファイルを読み込む(loadtxtのdelimiterのdefaultはwhitespace)
        data = np.loadtxt(txt)
        print(txt + "の出力ファイル名を入力してください．拡張子はいりません．")
        outputfile = input()
        outputfile += ".csv"
        f = open(outputfile, "a")
        filecsv = csv.writer(f)
        tmplist = data.tolist()
        filecsv.writerows(tmplist)
        f.close()
else:
    data = np.loadtxt(inputfile)
    #出力ファイルの作成
    print("出力ファイル名を入力してください．拡張子はいりません．")
    outputfile = input()
    outputfile += ".csv"
    f = open(outputfile, 'a')

    #出力ファイルに対してcsvで書き込むようなwriterオブジェクトを作成
    filecsv = csv.writer(f)

    #データファイルから読み込んだ2次元配列(numpy内で定義されている)をPython3の2次元Listに変換
    tmplist = data.tolist()

    #2次元Listを一気に出力ファイルにCSV形式で書き込む
    filecsv.writerows(tmplist)

    #ファイルを閉じる
    f.close()
