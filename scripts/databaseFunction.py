import config as cf
import MySQLdb

def sqlConnection():
    conn = MySQLdb.connect(cf.Hostname, cf.DBUserName, cf.DBPassword, cf.Database,charset='utf8')
    if conn.open:
        print "connected"
    else:
        print "Error in connection"
    return conn
# For insert new row , we use this function to insert posts and comments
