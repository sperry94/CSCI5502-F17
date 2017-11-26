import MySQLdb

class YelpDB:

    def __init__ (self, host="localhost", user="paul", passwd="weasels", db="yelp_db"):
        self.db = MySQLdb.connect (host, user, passwd, db)
        self.cursor = self.db.cursor()

    def getReviewIDs(self):
        num  = self.cursor.execute ("SELECT id from review")
        rows = self.cursor.fetchall()
        return rows
 
    def getReview(self, id):
        sql = ("SELECT stars, date, text, business_id, user_id FROM review WHERE id=%s")
        self.cursor.execute (sql, [id])
        return self.cursor.fetchone()

    def getBusinessIDs(self):
        num  = self.cursor.execute ("SELECT id from business")
        rows = self.cursor.fetchall()
        return rows

    def getBusiness(self, id):
        sql = ("SELECT name, city, state FROM business WHERE id=%s")
        self.cursor.execute (sql, [id])
        return self.cursor.fetchone()

    def getCategory(self, id):

        sql =  ("SELECT category FROM category WHERE business_id=%s")
        self.cursor.execute (sql, [id])
        return self.cursor.fetchone()

 
