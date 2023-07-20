import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root')
cur = db.cursor()
cur.execute('CREATE DATABASE Password_manager')

# ----------Table Creation----------
import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='Password_manager')
cur = db.cursor()
cur.execute("CREATE TABLE Accounts(userID int PRIMARY KEY AUTO_INCREMENT,Username VARCHAR(50),Password VARCHAR(30))")
cur.execute("CREATE TABLE userdata (Website VARCHAR(50),"
            "Username VARCHAR(50), "
            "Password VARCHAR(50), "
            "Email_id VARCHAR(50))"
            )
db.commit()

