import csv

with open('utilities/loanapp.csv') as f:
    csvReader = csv.reader(f, delimiter=',')
    # print(csvReader)
    # print(list(csvReader))
    names = []
    stats = []
    for row in csvReader:
        if len(row) > 0:
            names.append(row[0])
            stats.append(row[1])

print(names)
print(stats)
Index = names.index("Tim")
loanStatus = stats[Index]
print('Tim loan status is ' + loanStatus)

with open('utilities/loanapp.csv', 'a') as f1:
    write = csv.writer(f1)
    write.writerow(["Megan", "Accepted"])
    print(csvReader)
