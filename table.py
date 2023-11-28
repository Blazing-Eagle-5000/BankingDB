import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database = "bankdb"
)

mycursor = mydb.cursor()

try:
  mycursor.execute("DROP TABLE bankusers")
except:
  pass
mycursor.execute("CREATE TABLE bankusers (userid INT Primary key,password VARCHAR(255), username VARCHAR(255),mobileno VARCHAR(255),balance INT)")

print("Table successfully created!!")
