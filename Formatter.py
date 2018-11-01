import numpy as np
import pandas as pd
import csv

f = open('data.csv')
csv_f = csv.reader(f)


for row in csv_f:


    #print "[" + row[1],",",row[3],",",row[5],",",row[7],",",row[9] + "]"

    if row[1] != "EPR":
        EPR = float(row[1])
    else:
        EPR = "EPR"
    if row[3] != "NPR":
        NPR = float(row[3])
    else:
        NPR = "NPR"

    if row[5] != "APR":
        APR = float(row[5])
    else:
        APR = "APR"

    if row[7] != "CPR":
        CPR = float(row[7])
    else:
        CPR = "CPR"

    if row[9] != "OPR":
        OPR = float(row[9])
    else:
        OPR = "OPR"

    listy = [EPR, NPR, APR, CPR, OPR]
    #print listy

    reformer = [50.0, 20.0, 50.0, 90.0, 90.0]
    helper = [90.0, 20.0, 90.0, 60.0, 50.0]
    achiever = [60.0, 50.0, 40.0, 90.0, 90.0]
    individualist = [20.0, 20.0, 20.0, 50.0, 40.0]
    investigator = [20.0, 40.0, 50.0, 90.0, 60.0]
    loyalist = [50.0, 90.0, 20.0, 90.0, 40.0]
    enthusiast = [90.0, 90.0, 90.0, 20.0, 90.0]
    challenger = [90.0, 20.0, 20.0, 90.0, 60.0]
    peacemaker = [60.0, 20.0, 90.0, 40.0, 90.0]
    new_list = list()
    Rtemp = 0
    Htemp = 0
    Atemp = 0
    Itemp = 0
    Intemp = 0
    Ltemp = 0
    Etemp = 0
    Ctemp = 0
    Ptemp = 0

    for x in range(4):
        Rtemp += abs(listy[x] - reformer[x])

    for x in range(4):
        Htemp += abs(listy[x] - helper[x])

    for x in range(4):
        Atemp += abs(listy[x] - achiever[x])

    for x in range(4):
        Itemp += abs(listy[x] - individualist[x])

    for x in range(4):
        Intemp += abs(listy[x] - investigator[x])

    for x in range(4):
        Ltemp += abs(listy[x] - loyalist[x])

    for x in range(4):
        Etemp += abs(listy[x] - enthusiast[x])

    for x in range(4):
        Ctemp += abs(listy[x] - challenger[x])

    for x in range(4):
        Ptemp += abs(listy[x] - peacemaker[x])

    # print Rtemp
    # print Htemp
    # print Atemp
    # print Itemp
    # print Intemp
    # print Ltemp
    # print Etemp
    # print Ctemp
    # print Ptemp
    x = 400
    tempL = [Rtemp, Htemp, Atemp, Itemp, Intemp, Ltemp, Etemp, Ctemp, Ptemp]

    ##print min(tempL)
    minimum = min(tempL)
    if minimum == Rtemp:
        print "0, 0, 0, 0, 0"
    if minimum == Htemp:
        print "1, 0, 0, 0, 0"

    if minimum == Atemp:
        print "0, 1, 0, 0, 0"

    if minimum == Itemp:
        print "0, 0, 1, 0, 0"

    if minimum == Intemp:
        print "0, 0, 0, 1, 0"

    if minimum == Ltemp:
        print "0, 0, 0, 0, 1"

    if minimum == Etemp:
        print "1, 1, 0, 0, 0"

    if minimum == Ctemp:
        print "1, 1, 1, 0, 0"

    if minimum == Ptemp:
        print "1, 1, 1, 1, 0"
