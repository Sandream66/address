# -*- coding: utf-8 -*-
import csv
import sys


class MakeAddress():

    def __init__(self, zipcode, telname, mobilename):
        self.zipcode = zipcode
        self.telname = telname
        self.mobilename = mobilename
        self.newcsv = []
        self.filename = ""

    def get_filename(self, args):
        try:
            self.filename = args[1]
        except:
            pass
        return self.filename

    def csv_reader(self, filename):
        f = open(filename, 'r')
        reader = csv.DictReader(f)
        return reader

    def make_word(self, string, *args):
        return string.join(args)

    def make_new_csv(self, csvdic):
        top_list = [
                'name',
                'zip code',
                'address',
                'phone',
                'mobile_pyone'
                        ]
        self.newcsv.append(top_list)
        for i in csvdic:
            line = []
            line.append(self.make_word(" ", i['firstname'], i['lastname']))
            line.append(self.make_word(":", self.zipcode, i['zip code']))
            line.append(self.make_word(
                                        "",
                                        i['address1'],
                                        i['address2'],
                                        i['address3'],
                                    ))
            line.append(self.make_word(":", self.telname, i['phone']))
            line.append(self.make_word(":", self.mobilename, i['mobilephone']))
            self.newcsv.append(line)
        return self.newcsv

    def new_address(self):
        args = sys.argv
        filename = self.get_filename(args)
        if filename:
            csvdic = self.csv_reader(filename)
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
    test = MakeAddress("郵便番号", "電話番号", "携帯番号")
    test.write_csv("makeaddress_new.csv")
