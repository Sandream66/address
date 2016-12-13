# -*- coding: utf-8 -*-
# !/usr/bin/env python
import sys
import csv

args = sys.argv
# コマンドプロンプトで入力したファイル名を受け取る
try:
    filename = args[1]
except:
    sys.exit("No file Name!")

# 受け取ったファイル名をつかって該当のCSVを受け取る
try:
    filename = args[1]
    f = open(filename, 'r')
except IOError as e:
    sys.exit("Unable to open file: {}".format(e))

# 書き出すCSVの項目行の生成
newcsv = []
top_list = [
        'name',
        'zip code',
        'address',
        'phone',
        'mobile_pyone'
                ]
newcsv.append(top_list)
for i in csv.DictReader(f):
    line = []
    line.append(" ".join((i['lastname'], i['firstname'])))
    line.append(":".join(("郵便番号", i['zip code'])))
    line.append("".join((i['address1'], i['address2'], i['address3'])))
    line.append("：".join(("電話番号", i['phone'])))
    line.append("：".join(("携帯番号", i['mobilephone'])))
    newcsv.append(line)

# 生成したデータの書き出し
writer = csv.writer(open("allcodelist.csv", "w"), lineterminator='\n')
writer.writerows(newcsv)

f.close()
