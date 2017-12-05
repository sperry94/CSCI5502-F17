#!/opt/local/bin/python2.7

import sys
import YelpDB
from Process import Process

class BusinessProcessor (Process):

    ### This class exists purely to override Process from the base
    def __init__ (self, fileName):
        super (BusinessProcessor, self).__init__(fileName)
        self.businesses = {}

    ### This class exists purely to override Process from the base
    #
    def process (self, stars, text, business_id, user_id):

        if business_id in self.businesses:
            self.businesses[business_id] += 1
        else:
            self.businesses[business_id]  = 1


if len(sys.argv) < 2:
    print "\nProvide a review id list file as an argument\n"
    sys.exit (-1)
else: 
    reviewIDsFile = sys.argv[1]

processor = BusinessProcessor(reviewIDsFile)
processor.loop()

for key, value in sorted(processor.businesses.iteritems(), key=lambda (k, v): (v, k)):
    print "%s %d" % (key, processor.businesses[key])
