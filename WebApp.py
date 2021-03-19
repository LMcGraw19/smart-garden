from flask import Flask, request, render_template
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
#from flask_sqlalchemy import SQLAlchemy #No longer using this module
import mysql.connector #Module that connects us to the database

app = Flask(__name__)
api = Api(app)

#Currently unused code
#class Hello(Resource):
#    def get(self, name):
#        return names[name]
#    
#    def post(self):
#        return{"data": "Hello World"}
#
#api.add_resource(Hello, "/<string:name>")

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/Charts')
def sensors():
    return render_template('charts.html');

@app.route('/BME280')
def smartgarden():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Smartgarden",
      database="SmartGarden"
    )
    mycursor = mydb.cursor()
    
    mycursor.execute('SELECT * FROM BME280')
    mycursor.fetchall() #This and the line above need to be used for the program to know how many rows their are.
    
    list_row = [] #Empty list for holding the row count
    
    list_row.append(mycursor.rowcount - 5) #Gives us a row count of the table which will be used inthe MYSQL statement below
    
    if list_row[0] < 0: #If statement to make sure the offset value given will not be a negative number
        list_row[0] = 0
    
    list_row = tuple(list_row) #The variable given in the below statement must be a tuple. This is all why a list was used initally and not a string or int
    
    
    sql = "SELECT * FROM BME280 LIMIT 5 OFFSET %s" # MYSQL statement
    
    mycursor.execute(sql, list_row) #Statement that executes the MYSQL statement with the variable defined within.
    myresult = mycursor.fetchall() #fetchall gives us the answer from the MYSQL statement
    timelist = []
    templist = []
    preslist = []
    altilist = []
    humiditylist = []
    
    for row in myresult:
        timelist.append(row[1])
        templist.append(row[2])
        preslist.append(row[3])
        altilist.append(row[4])
        humiditylist.append(row[5])
        
    
    return render_template('BME280.html', time=timelist, temp=templist, pres=preslist, alti=altilist, humi=humiditylist);#For now the html page is given a list with tuples in it.
    
@app.route('/DS18B20')
def DS18B20():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Smartgarden",
      database="SmartGarden"
    )
    mycursor = mydb.cursor()
    
    mycursor.execute('SELECT * FROM DS18B20')
    mycursor.fetchall() #This and the line above need to be used for the program to know how many rows their are.
    
    list_row = [] #Empty list for holding the row count
    
    list_row.append(mycursor.rowcount - 5) #Gives us a row count of the table which will be used inthe MYSQL statement below
    
    if list_row[0] < 0: #If statement to make sure the offset value given will not be a negative number
        list_row[0] = 0
    
    list_row = tuple(list_row) #The variable given in the below statement must be a tuple. This is all why a list was used initally and not a string or int
    
    
    sql = "SELECT * FROM DS18B20 LIMIT 5 OFFSET %s" # MYSQL statement
    
    mycursor.execute(sql, list_row) #Statement that executes the MYSQL statement with the variable defined within.
    myresult = mycursor.fetchall() #fetchall gives us the answer from the MYSQL statement
    timelist = []
    templist = []
    
    for row in myresult:
        timelist.append(row[1])
        templist.append(row[2])        
    
    return render_template('DS18B20.html', time=timelist, temp=templist);#For now the html page is given a list with tuples in it.
  
@app.route('/SEN0114')
def SEN0114():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Smartgarden",
      database="SmartGarden"
    )
    mycursor = mydb.cursor()
    
    mycursor.execute('SELECT * FROM SEN0114')
    mycursor.fetchall() #This and the line above need to be used for the program to know how many rows their are.
    
    list_row = [] #Empty list for holding the row count
    
    list_row.append(mycursor.rowcount - 5) #Gives us a row count of the table which will be used inthe MYSQL statement below
    
    if list_row[0] < 0: #If statement to make sure the offset value given will not be a negative number
        list_row[0] = 0
    
    list_row = tuple(list_row) #The variable given in the below statement must be a tuple. This is all why a list was used initally and not a string or int
    
    
    sql = "SELECT * FROM SEN0114 LIMIT 5 OFFSET %s" # MYSQL statement
    
    mycursor.execute(sql, list_row) #Statement that executes the MYSQL statement with the variable defined within.
    myresult = mycursor.fetchall() #fetchall gives us the answer from the MYSQL statement
    timelist = []
    moislist = []
    
    for row in myresult:
        timelist.append(row[1])
        moislist.append(row[2])        
    
    return render_template('SEN0114.html', time=timelist, mois=moislist);#For now the html page is given a list with tuples in it.
    
@app.route('/SHT21')
def SHT21():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Smartgarden",
      database="SmartGarden"
    )
    mycursor = mydb.cursor()
    
    mycursor.execute('SELECT * FROM SHT21')
    mycursor.fetchall() #This and the line above need to be used for the program to know how many rows their are.
    
    list_row = [] #Empty list for holding the row count
    
    list_row.append(mycursor.rowcount - 5) #Gives us a row count of the table which will be used inthe MYSQL statement below
    
    if list_row[0] < 0: #If statement to make sure the offset value given will not be a negative number
        list_row[0] = 0
    
    list_row = tuple(list_row) #The variable given in the below statement must be a tuple. This is all why a list was used initally and not a string or int
    
    
    sql = "SELECT * FROM SHT21 LIMIT 5 OFFSET %s" # MYSQL statement
    
    mycursor.execute(sql, list_row) #Statement that executes the MYSQL statement with the variable defined within.
    myresult = mycursor.fetchall() #fetchall gives us the answer from the MYSQL statement
    timelist = []
    templist = []
    humilist = []
    
    for row in myresult:
        timelist.append(row[1])
        templist.append(row[2])        
        humilist.append(row[3])
        
    return render_template('SHT21.html', time=timelist, temp=templist, humi=humilist);#For now the html page is given a list with tuples in it.
    
@app.route('/TSL2591')
def TSL2591():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Smartgarden",
      database="SmartGarden"
    )
    mycursor = mydb.cursor()
    
    mycursor.execute('SELECT * FROM TSL2591')
    mycursor.fetchall() #This and the line above need to be used for the program to know how many rows their are.
    
    list_row = [] #Empty list for holding the row count
    
    list_row.append(mycursor.rowcount - 5) #Gives us a row count of the table which will be used inthe MYSQL statement below
    
    if list_row[0] < 0: #If statement to make sure the offset value given will not be a negative number
        list_row[0] = 0
    
    list_row = tuple(list_row) #The variable given in the below statement must be a tuple. This is all why a list was used initally and not a string or int
    
    
    sql = "SELECT * FROM TSL2591 LIMIT 5 OFFSET %s" # MYSQL statement
    
    mycursor.execute(sql, list_row) #Statement that executes the MYSQL statement with the variable defined within.
    myresult = mycursor.fetchall() #fetchall gives us the answer from the MYSQL statement
    timelist = []
    lumilist = []
    
    for row in myresult:
        timelist.append(row[1])
        lumilist.append(row[2])        
        
    return render_template('TSL2591.html', time=timelist, lumi=lumilist);#For now the html page is given a list with tuples in it.

def connect():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Smartgarden",
      database="SmartGarden"
    )
    mycursor = mydb.cursor()
    return(mycursor)
    
if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=True, host='127.0.0.1', port=5020)
