#!/opt/local/bin/python2.7

import sys
import random
import YelpDB

### Ensure an argument was given 
if len(sys.argv) != 2:
   print "\n *** Please provide the business id to select reviews from *** \n"
   sys.exit (0)

### Connect to the database and get all the IDs
ydb       = YelpDB.YelpDB()
reviewIDs = ydb.getReviewIDs(sys.argv[1])

### Loop until we've pulled the limit number of review IDs
for id in reviewIDs:
    print id[0]
