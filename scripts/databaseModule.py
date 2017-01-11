import MySQLdb as db
import config as cf


class MySQL:
    # Initializing the database in the constructor
    def __init__(self):
        try:
            self.con = db.connect(cf.Hostname, cf.DBUserName, cf.DBPassword, cf.Database,charset='utf8')
            self.cur = self.con.cursor()
        except  Exception as e:
            print "Could not connect to server ... ", e

    def selectAllFrom(self, tableName):

        query = "SELECT * FROM " + tableName

        self.cur.execute(query)
        return self.cur.fetchall()

    # *args contains the column names to select from the table
    def selectColFrom(self, tableName, *args):

        query = "SELECT "

        for i, colName in enumerate(args):
            query += colName + ", " if i < (len(args) - 1) else colName

        query += " FROM " + tableName

        self.cur.execute(query)
        return self.cur.fetchall()
