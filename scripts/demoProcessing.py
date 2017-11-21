#!/opt/local/bin/python2.7

import sys
from Process import Process

class AnotherProcessor (Process):

    ### This class exists purely to override Process from the base
    #
    def process (self, stars, text, business_id, user_id):
       
        ### Print it out
        print "\nDifferent Stars:       %d" % stars
        print "\nDifferent Text:        %s" % text
        print "\nDifferent Business ID: %s" % business_id
        print "\nDifferent User ID:     %s" % user_id
        print "\n"
 

if len(sys.argv) < 2:
    print "\nProvide a review id list file as an argument\n"
    sys.exit (-1)
else: 
    reviewIDsFile = sys.argv[1]

processor = Process(reviewIDsFile)
processor.loop()

raw_input ("Hit return to process with the new processor")

processor = AnotherProcessor (reviewIDsFile)
processor.loop()
