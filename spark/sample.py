import sys
import string
import os
import csv
import random





FirstLine = 1
prevKey = None
date = 1
outfile = None
with open('part-00000.csv', 'r') as infile:
    next(infile)
    for row in infile:
        curKey = row[2:10]
       # print curKey
        if(curKey != prevKey):
            if FirstLine != 1:
                FirstLine = 0
                outfile.close()
            fileName = str(date)+'.csv'
            outfile = open(fileName, 'w')
            outfile.write("VendorID,pickup_datetime,pickup_longitude,pickup_lattitude,fare_amount,tip_amount,passenger_count,trip_distance\n")
            outfile.write(row)
            prevKey = curKey
            date = date + 1
        else:
            Y = random.sample([1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,15], 1)
            if int(Y[0]) == 1:
                outfile.write(row)
                prevKey = curKey
    outfile.close()

