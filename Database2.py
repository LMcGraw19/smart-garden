import mysql.connector #Module for connection to mysql server
import Databasetable

mydb = mysql.connector.connect( #Server info goes here
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor() #Connect server info with a variable

mycursor.execute("CREATE DATABASE SmartGarden") #Create database

Databasetable.main() #Calls module that creates tables with nonsence data
