#Wakif Ferdous
#1770041

import csv
filename= input()
with open(filename, 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    result = dict()
    for i in reader:
        for j in i:
            if j in result:
                result[j] = result[j] + 1
            else:
                result[j] = 1
    for k in list(result.keys()):
        print("{} {}".format(k, result[k]))




