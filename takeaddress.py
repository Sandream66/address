# -*- coding: utf-8 -*-
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
            line.append(self.make_word(":", self.telname, i['phone']))
            line.append(self.make_word(":", self.mobilename, i['mobilephone']))
            line.append(self.make_word(":", self.zipcode, i['zip code']))
            line.append(self.make_word(
                                        "",
                                        i['address1'],
                                        i['address2'],
                                        i['address3'],
                                    ))
            self.newcsv.append(line)
        return self.newcsv

if __name__ == '__main__':
    test = TakeAddress("郵便番号", "電話番号", "携帯番号")
    test.write_csv("takeaddress_new.csv")
