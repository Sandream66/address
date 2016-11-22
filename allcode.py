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
            name = " ".join((i['lastname'], i['firstname']))
            zip_code = ":".join(("郵便番号", i['zip code']))
            address = "".join((i['address1'], i['address2'], i['address3']))
            phone = "：".join(("電話番号", i['phone']))
            mobilephone = "：".join(("携帯番号", i['mobilephone']))
            line.append(name)
            line.append(zip_code)
            line.append(address)
            line.append(phone)
            line.append(mobilephone)
            newcsv.append(line)

        fh = open("allcode.csv", "w")
        writer = csv.writer(fh, lineterminator='\n')
        writer.writerows(newcsv)

        f.close()
        fh.close()
except:
    print("no filename")
