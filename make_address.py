# -*- coding: utf-8 -*-
# !/usr/bin/env python
import os
import csv


class MakeAddress():
    LINETERMINATOR = os.linesep
    DEFAULT_ENCODING = 'sjis'

    def __init__(self, filename, encoding=DEFAULT_ENCODING):
        self.filename = filename
        self.encoding = encoding

    def make_new_csv_title(self, old_title):
        """
        新しいcsvのtitle(1行目)を返す

        既存のタイトルが必要な可能性があるので引数で貰う
        """
        return [
            'name',
            'zip code',
            'address',
            'phone',
            'mobile_phone',
        ]

    def make_new_csv_row(self, old_row):
        """
        既存のcsvの行を受け取り，新しいcsvの行を作る
        """
        line = []
        line.append(" ".join((old_row['lastname'], old_row['firstname'])))
        line.append(":".join(("郵便番号", old_row['zip code'])))
        line.append("".join((old_row['address1'],
                             old_row['address2'],
                             old_row['address3'])))
        line.append("：".join(("電話番号", old_row['phone'])))
        line.append("：".join(("携帯番号", old_row['mobilephone'])))
        return line

    def str_convert(self, s):
        """
        python2系の場合はunicode型をstr型にする必要がある
        """

    def make_new_csv(self):
        """
        既存のcsvを1行ずつ読み込んで1行ずつ返す
        """
        with open(self.filename, 'r', encoding=self.encoding) as f:
            reader = csv.DictReader(f)
            for index, row in enumerate(reader):
                if index == 0:
                    # 1行目の場合は先にタイトルを返す
                    yield self.make_new_csv_title(row.keys())
                # 既存csvから1行ずつ新しい行を作成する
                yield self.make_new_csv_row(row)

    def write_csv(self, new_filename):
        with open(new_filename, 'w', encoding=self.encoding) as f:
            writer = csv.writer(f, lineterminator=MakeAddress.LINETERMINATOR)
            for new_row in self.make_new_csv():
                writer.writerow(new_row)


if __name__ == '__main__':
    obj = MakeAddress('addresslist.csv')
    obj.write_csv('addresslist_new.csv')
