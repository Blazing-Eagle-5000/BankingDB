import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin"
)

mycursor = mydb.cursor()
try:
  mycursor.execute("DROP DATABASE bankdb")
except:
  pass
mycursor.execute("CREATE DATABASE bankdb")

print("Database created successfully!!")