import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database = "bankdb"
  )

mycursor = mydb.cursor(buffered=True)

x = int(input("Enter UserID: "))
z = input("Enter UserName: ")
y = input("Enter Password: ")
u = input("Enter MobileNo: ")
v = 0

a = "INSERT INTO bankusers (userid,password,username,mobileno,balance) VALUES (%s,%s,%s,%s,%s)"
b = (x,y,z,u,v)
mycursor.execute(a,b)

mycursor.execute("SELECT * FROM bankusers")
mydb.commit()

print("You have successfully registered!!")

myresult = mycursor.fetchall()
for x in myresult:
  print(x)