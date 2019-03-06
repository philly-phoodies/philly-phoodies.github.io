import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "",
                           db = "PhillyPhoodies")
    c = conn.cursor()

    return c, conn
