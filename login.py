import mysql.connector
import sys

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database = "bankdb"
  )

mycursor = mydb.cursor()

a=input("Enter UserName: ")

sql = "SELECT password FROM bankusers WHERE username=('"+a+"')"
mycursor.execute(sql)
p = mycursor.fetchall()
if (p==[]):
  print("Enter a correct UserName!!")
  sys.exit()

b=input("Enter Password: ")

if (b==p[0][0]):
  x = "SELECT balance FROM bankusers WHERE username=('"+a+"')"
  mycursor.execute(x)
  y = mycursor.fetchall()
  print()
  print("Welcome back",a+"!!")
  print("Your balance is: "+str(y[0][0])+"$")
else:
  print("Enter the correct Password!!")
  sys.exit()
  
while True:
  print()
  print("What would you like to do?")
  print("Press 'a' to deposit money")
  print("Press 'b' to withdraw money")
  print("Press 'c' to transfer money")
  print("Press 'd' to logout")
  print()
  output = input("Enter your choice: ")
  print()
  match output:

    case 'a':
      x = input("Enter amount to Deposit: ")
      if (int(x)<=0):
        print("Enter a postive value to Transfer: ")
        sys.exit()
      q=("UPDATE bankusers SET balance=balance+"+x+" WHERE username='"+a+"'")
      mycursor.execute(q)
      mydb.commit()
      x = "SELECT balance FROM bankusers WHERE username=('"+a+"')"
      mycursor.execute(x)
      y = mycursor.fetchall()
      print("Your balance is: "+str(y[0][0])+"$")

    case 'b':
      x = input("Enter amount to Withdraw: ")
      if (int(x)<=0):
        print("Enter a postive value to Withdraw: ")
        sys.exit()
      q=("UPDATE bankusers SET balance=balance-"+x+" WHERE username='"+a+"'")
      mycursor.execute(q)
      mydb.commit()
      x = "SELECT balance FROM bankusers WHERE username=('"+a+"')"
      mycursor.execute(x)
      y = mycursor.fetchall()
      print("Your balance is: "+str(y[0][0])+"$")
      
    case "c":
      x = input("Enter amount to Transfer: ")
      if (int(x)<=0):
        print("Enter a postive value to Transfer: ")
        sys.exit()
      n = input("Enter name of Recipient: ")
      sql = "SELECT userid FROM bankusers WHERE username=('"+n+"')"
      mycursor.execute(sql)
      p = mycursor.fetchall()
      if (p==[]):
        print("Enter the name of Recipient correctly!!")
        sys.exit()
      q=("UPDATE bankusers SET balance=balance-"+x+" WHERE username='"+a+"'")
      mycursor.execute(q)
      mydb.commit()
      q=("UPDATE bankusers SET balance=balance+"+x+" WHERE username='"+n+"'")
      mycursor.execute(q)
      mydb.commit()
      x = "SELECT balance FROM bankusers WHERE username=('"+a+"')"
      mycursor.execute(x)
      y = mycursor.fetchall()
      print("Your balance is: "+str(y[0][0])+"$")
      x = "SELECT balance FROM bankusers WHERE username=('"+n+"')"
      mycursor.execute(x)
      y = mycursor.fetchall()
      print(n+"'s balance is: "+str(y[0][0])+"$")
    case 'd':
      print("You have been logged out!!")
      sys.exit()
