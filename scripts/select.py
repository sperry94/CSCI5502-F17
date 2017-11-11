#!/opt/local/bin/python2.7

import sys
import random
import YelpDB

### Ensure an argument was given 
if len(sys.argv) != 2:
   print "\n *** Please provide a number of reviews to randomly select *** \n"
   sys.exit (0)
else:
   limit = int(sys.argv[1])

### Connect to the database and get all the IDs
ydb       = YelpDB.YelpDB()
reviewIDs = ydb.getReviewIDs()

### This will contain a hash of the review ids selected
selected = {}

### This is a list of the business categories we accept
restaurants = []
restaurants.append('Restaurants')

### Loop until we've pulled the limit number of review IDs
while len(selected) < limit:

    ### Generate a random number between 0 and the number of IDs
    index = random.randint (0, len(reviewIDs))
    id = reviewIDs[index]

    ### Pull the review, then the business, and the business category
    (stars, date, text, business_id, user_id) = ydb.getReview(id)
    (name, city, state) = ydb.getBusiness (business_id)
    (category)          = ydb.getCategory (business_id)

    ### If the review has not been selected and it is in the lis
    ### of acceptable categories, keep it.
    try:
        if id not in selected and category[0] == 'Restaurants':
            selected[id] = 1 
    except:
        continue

### When done, dump all the IDs
for id in selected:
    print id[0]
