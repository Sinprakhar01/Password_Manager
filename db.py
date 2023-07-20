import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='45968060')
cur = db.cursor()
cur.execute('CREATE DATABASE datm')

# ----------Table Creation----------
import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='45968060',
    database='datm')
cur = db.cursor()
cur.execute("CREATE TABLE useraccounts (userID int PRIMARY KEY AUTO_INCREMENT,mail_id VARCHAR(50),password VARCHAR(30))")
cur.execute("CREATE TABLE userdata (Website VARCHAR(50),"
            "Username VARCHAR(50), "
            "Password VARCHAR(50), "
            "Email_id VARCHAR(50))"
            )
db.commit()

