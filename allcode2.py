# -*- coding: utf-8 -*-

import sys
import csv

args = sys.argv

filename = args[1]

f = open(filename, 'r')

for i in csv.DictReader(f):
    name = " ".join((i['lastname'], i['firstname']))
    print(name)