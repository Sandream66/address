# -*- coding: utf-8 -*-

"""
http://ur0.pw/zMDN
"""

import csv
import sys

args = sys.argv
filename = ""
try:
    filename = args[1]
    if filename:
        f = open(filename, 'r')
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
            name = "%s %s" % (i['lastname'], i['firstname'])
            zip_code = "郵便番号:%s" % (i['zip code'])
            address = "%s%s%s" % (i['address1'], i['address2'], i['address3'])
            phone = "電話番号：%s" % (i['phone'])
            mobilephone = "携帯番号：%s" % (i['mobilephone'])
            line.append(name)
            line.append(zip_code)
            line.append(address)
            line.append(phone)
            line.append(mobilephone)
            newcsv.append(line)

        f = open("allcode.csv", "w")
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(newcsv)

        f.close()
except:
    print("no filename")