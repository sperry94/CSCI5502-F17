#!/opt/local/bin/python2.7

import sys
import random
import YelpDB

### Ensure an argument was given 
if len(sys.argv) != 2:
   print "\n *** Please provide the city to select reviews from *** \n"
   sys.exit (0)

### Connect to the database and get all the IDs
ydb       = YelpDB.YelpDB()
reviewIDs = ydb.getReviewIDCity(sys.argv[1])

### This will contain a hash of the review ids selected
selected = {}

### This is a list of the business categories we accept
restaurants = []
restaurants.append('Restaurants')

### Loop until we've pulled the limit number of review IDs
for id in reviewIDs:

    ### Pull the review, then the business, and the business category
    (stars, date, text, business_id, user_id) = ydb.getReview(id)
    (name, city, state) = ydb.getBusiness (business_id)
    (category)          = ydb.getCategory (business_id)

    ### If the review has not been selected and it is in the lis
    ### of acceptable categories, keep it.
    try:
        if id not in selected and category[0] == 'Restaurants':
            selected[id] = 1 
            if len(selected)>=10000:
               break
    except:
        continue

### When done, dump all the IDs
for id in selected:
    print id[0]
