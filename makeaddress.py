# -*- coding: utf-8 -*-
# !/usr/bin/env python
import csv


class MakeAddress():

    def __init__(self, filename):
        self.filename = filename

    def csv_reader(self, filename):
        f = open(filename, 'r')
        reader = csv.DictReader(f)
        return reader

    def make_new_csv(self, csvdic):
        newcsv = []
        top_list = [
                'name',
                'zip code',
                'address',
                'phone',
                'mobile_pyone'
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
            csvdic = self.csv_reader(self.filename)
            newcsv = self.make_new_csv(csvdic)
            return newcsv

    def write_csv(self, newfilename):
        newcsv = self.new_address()
        if self.filename:
            f = open(newfilename, "w")
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(newcsv)
            f.close()
        else:
            print("no filename")

if __name__ == '__main__':
    test = MakeAddress("addresslist.csv")
    test.write_csv("makeaddress_new.csv")
