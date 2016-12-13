# -*- coding: utf-8 -*-
# !/usr/bin/env python
from makeaddress import MakeAddress


class TakeAddress(MakeAddress):

    def make_new_csv(self, csvdic):
        top_list = [
                'name',
                'phone',
                'mobile_pyone',
                'zip code',
                'address'
                        ]
        self.newcsv.append(top_list)
        for i in csvdic:
            line = []
            line.append(self.make_word(" ", i['firstname'], i['lastname']))
            line.append(self.make_word(":", "固定電話", i['phone']))
            line.append(self.make_word(":", "モバイル", i['mobilephone']))
            line.append(self.make_word(":", "郵便番号", i['zip code']))
            line.append(self.make_word(
                                        "",
                                        i['address1'],
                                        i['address2'],
                                        i['address3'],
                                    ))
            self.newcsv.append(line)
        return self.newcsv

if __name__ == '__main__':
    test = TakeAddress("addresslist.csv")
    test.write_csv("takeaddress_new.csv")
