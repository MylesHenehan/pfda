# Programme which outputs entries from a CSV file as a list

import csv

FILENAME = "data.csv"
DATADIR = "../week-1/"

with open(DATADIR + FILENAME, "r") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    for line in reader:
        if linecount == 0:
            print (f"{line}\n-------------------")
        else:
            print(line)
        linecount += 1
       
        

