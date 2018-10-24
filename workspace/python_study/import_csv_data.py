import csv

csvfile = open('data-text.csv', 'r')
reader = csv.DictReader(csvfile)

for row in reader:
    print(row)