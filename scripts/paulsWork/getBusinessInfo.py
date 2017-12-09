#!/opt/local/bin/python2.7

import sys
import random
import pdb

import YelpDB

### Ensure an argument was given 
if len(sys.argv) != 2:
   print "\n *** Please provide the file of business IDs to process\n"
   sys.exit (0)

fileHandle = open (sys.argv[1])

### Connect to the database and get all the IDs
ydb = YelpDB.YelpDB()

### Read and get all the business Info for the list of business IDs
for line in fileHandle:
    (id, frequency) = line.split()
    (name, city, state) = ydb.getBusiness (id)
    print "ID:  %s  Frequency: %s  Name: %s  City:  %s  State:  %s" % (id, frequency, name, city, state)
