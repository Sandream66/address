# -*- coding: utf-8 -*-
# !/usr/bin/env python
from makeaddress import MakeAddress


class TakeAddress(MakeAddress):

    def make_new_csv(self, csvdic):
        newcsv = []
        top_list = [
                'name',
                'phone',
                'mobile_pyone',
                'zip code',
                'address'
                        ]
        newcsv.append(top_list)
        for i in csvdic:
            line = []
            line.append(" ".join((i['lastname'], i['firstname'])))
            line.append("：".join(("TEL", i['phone'])))
            line.append("：".join(("MOBILE", i['mobilephone'])))
            line.append(":".join(("〒", i['zip code'])))
            line.append("".join((i['address1'], i['address2'], i['address3'])))
            newcsv.append(line)
        return newcsv

if __name__ == '__main__':
    test = TakeAddress("addresslist.csv")
    test.write_csv("takeaddress_new.csv")
