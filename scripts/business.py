#!/opt/local/bin/python2.7

import YelpDB

ydb = YelpDB.YelpDB()
businessIDs = ydb.getBusinessIDs()

cities     = {}
categories = {}

print "\nThere are %d businesses in the database\n" % len(businessIDs)

for id in businessIDs:

    (name, city, state) = ydb.getBusiness (id)
    (category)          = ydb.getCategory (id)

    try:
        if category[0] in categories:
            categories[category[0]] += 1 
        else:
            categories[category[0]]  = 1 
    except:
        continue
 
    if city in cities:
        cities[city] += 1 
    else:
        cities[city]  = 1 

'''
for city in sorted(cities):
    print city, cities[city]
print "\n\n"
'''

for key, value in sorted(cities.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print "%s: %s" % (key, value)

for key, value in sorted(categories.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print "%s: %s" % (key, value)

