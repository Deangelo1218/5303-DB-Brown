import os
import csv 
import json

with open('api/sqlzoo/test.csv', 'rb') as f:
    reader = csv.reader(f)
    newcsvdict = {"first name": [], "last name": []}
    for row in reader:
        first = row[0].split()[0]
        last = row[0].split()[1]
        newcsvdict["first name"].append(first)
        newcsvdict["last name"].append(last)


print(newcsvdict)