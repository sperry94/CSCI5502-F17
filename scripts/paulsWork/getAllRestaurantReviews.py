#!/opt/local/bin/python2.7

import sys
import random
import YelpDB

### Connect to the database and get all the IDs
ydb       = YelpDB.YelpDB()
reviewIDs = ydb.getReviewIDs()

### This will contain a hash of the review ids selected
selected = {}

### Loop until we've pulled the limit number of review IDs
for id in reviewIDs:

    ### Pull the review, then the business, and the business category
    (stars, date, text, business_id, user_id) = ydb.getReview(id)
    (name, city, state) = ydb.getBusiness (business_id)
    (category)          = ydb.getCategory (business_id)

    ### If the review has not been selected and it is in the lis
    ### of acceptable categories, keep it.
    try:
        if category[0] == 'Restaurants':
            print id[0]
    except:
        continue
