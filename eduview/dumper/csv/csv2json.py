import csv
import json

csvfile = open('admissions.csv', 'r')
jsonfile = open('out.json', 'w')

reader = csv.DictReader(csvfile)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')