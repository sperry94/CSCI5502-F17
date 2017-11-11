#!/opt/local/bin/python2.7

import sys
import YelpDB

def processReviews(stars, text, business_id, user_id):

    ### Print it out
    print "\nStars:       %d" % stars
    print "\nText:        %s" % text
    print "\nBusiness ID: %s" % business_id
    print "\nUser ID:     %s" % user_id
    print "\n"
 
ydb = YelpDB.YelpDB()

if len(sys.argv) < 2:
    print "\nProvide a review id list file as an argument\n"
else:
    with open(sys.argv[1]) as reviewIDsFile:    
        for nextID in reviewIDsFile:

            nextID=nextID.rstrip()
            print nextID

            ### Pull the review
            (stars, date, text, business_id, user_id) = ydb.getReview (nextID)

            processReviews (stars, text, business_id, user_id)
            raw_input()

