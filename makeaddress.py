# -*- coding: utf-8 -*-
# !/usr/bin/env python
import csv


class MakeAddress():

    def __init__(self, filename):
        self.filename = filename

    def csv_reader(self):
        f = open(self.filename, 'r', encoding='sjis')
        reader = csv.DictReader(f)
        return reader

    def make_new_csv(self, csvdic):
        newcsv = []
        top_list = [
            'name',
            'zip code',
            'address',
            'phone',
            'mobile_phone',
        ]
        newcsv.append(top_list)
        for i in csvdic:
            line = []
            line.append(" ".join((i['lastname'], i['firstname'])))
            line.append(":".join(("郵便番号", i['zip code'])))
            line.append("".join((i['address1'], i['address2'], i['address3'])))
            line.append("：".join(("電話番号", i['phone'])))
            line.append("：".join(("携帯番号", i['mobilephone'])))
            newcsv.append(line)
        return newcsv

    def new_address(self):
        if self.filename:
            csvdic = self.csv_reader()
            newcsv = self.make_new_csv(csvdic)
            return newcsv

    def write_csv(self, newfilename):
        assert self.filename, "no filename"
        newcsv = self.new_address()
        with open(newfilename, "w") as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(newcsv)

if __name__ == '__main__':
    test = MakeAddress("addresslist.csv")
    test.write_csv("makeaddress_new.csv")
