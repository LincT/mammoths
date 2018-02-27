import csv
mamoth_data = []

with open('pbdb_data.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    columns = reader.__next__()

    for row in reader:
        name = row[9]
