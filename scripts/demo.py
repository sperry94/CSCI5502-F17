#!/opt/local/bin/python2.7

import YelpDB

ydb = YelpDB.YelpDB()
reviewIDs = ydb.getReviewIDs()

print "\nThere are %d reviews in the database\n" % len(reviewIDs)

while 1:

   ### Get the index of the review to pull
   index = raw_input ("Enter an index from 0 to %d (or \"done\" to quit):" % len(reviewIDs))

   print "xxx%sxxx" % reviewIDs[int(index)]

   ### Quit if done
   if index == 'done':
      break

   ### Pull the review
   (stars, date, text, business_id, user_id) = ydb.getReview (reviewIDs[int(index)])

   '''
   ### Print it out
   print "\nStars:       %d" % stars
   print "\nText:        %s" % text
   print "\nBusiness ID: %s" % business_id
   print "\nUser ID:     %s" % user_id
   print "\n"
   '''
