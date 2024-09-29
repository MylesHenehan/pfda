# Programme which outputs averages ages from a csv fil

import csv

FILENAME = "data.csv"
DATADIR = "../week-1/"

with open(DATADIR + FILENAME, "r") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    sumofage = 0
    for line in reader:
        if linecount == 0:
            pass
        else:
            print(line)
            sumofage += int(line[1])
        linecount += 1

print(f"The sum of age is {sumofage}")
print(f"The average age is {int(sumofage/(linecount-1))}")
