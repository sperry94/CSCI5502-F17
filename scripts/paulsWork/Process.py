#!/opt/local/bin/python2.7

import YelpDB

class Process (object):

    def __init__(self, reviewIDs=""):
        self.__ydb       = YelpDB.YelpDB()
        self.__file      = open (reviewIDs)

    def process (self, stars, text, business_id, user_id):

        ### Print it out
        print "\nStars:       %d" % stars
        print "\nText:        %s" % text
        print "\nBusiness ID: %s" % business_id
        print "\nUser ID:     %s" % user_id
        print "\n"
 
    def loop (self ):
        i=0
        for nextID in self.__file:
            nextID=nextID.rstrip()
            #print "***** Review ***** %i %s" % (i,nextID)
            i=i+1
            (stars, date, text, business_id, user_id) = self.__ydb.getReview (nextID)
            self.process (stars, text, business_id, user_id)
