import csv

with open('utilities/loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    # print(csvReader)
    # print(list(csvReader))
    names = []
    statuses = []
    for row in csvReader:
        #print(row)
        names.append(row[0])
        statuses.append(row[1])

print(names)
print(statuses)
# Index = names.index('Sam')
# loanStatus = statuses[Index]
# print(f'Sam loan staus is {loanStatus}')

# for name in names:
#     print(name, f'loan status is {statuses[names.index(name)]}')

with open('utilities/loanapp.csv','a') as csvwFile:
    write = csv.writer(csvwFile)
    write.writerow(["Bob","Rejected"])
