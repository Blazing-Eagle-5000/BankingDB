import mysql.connector
import sys

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database = "bankdb"
  )

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM bankusers")

myresult = mycursor.fetchall()
for x in myresult:
  print(x)