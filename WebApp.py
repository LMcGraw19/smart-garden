from flask import Flask, request, render_template, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
#from flask_sqlalchemy import SQLAlchemy #No longer using this module
import mysql.connector #Module that connects us to the database
import requests
import sys
import json
#import paho.mqtt.client as mqtt
import time

app = Flask(__name__)
api = Api(app)

#@app.route('/database', methods=['POST'])
#def database():
#    print('running', file=sys.stdout)
#    data = request.get_json()
#    result = json.dumps(data)
    
#    sql = str(data.keys())
#    sql = sql[12:-3:]
#    values = str(data.values())
#    values = values[14:-3:]
#    values = values.split(',')
#    values[0] = values[0][1:-1:]
    
#    for val in range(len(values)):
#        if val != 0:
#            values[val] = float(values[val])        
    
#    sqlupdate(sql, values)
    
    
#    print(sql, file=sys.stdout)
#    print(values, file=sys.stdout)
        
    
#    returnvalue = {'Update':'Complete'}
#    return(returnvalue)

#def sqlupdate(sql, values):
#    mydb = mysql.connector.connect(
#      host="localhost",
#      user="root",
#      password="Smartgarden",
#      database="SmartGarden"
#    )
#    mycursor = mydb.cursor()
    
#    values = tuple(values)
    
#    if sql == 'BME280':
#        column = 'INSERT INTO BME280 (time, Temperature, Pressure, Altitude, Humidity) VALUES (%s, %s, %s, %s, %s)'
#    print(values, file=sys.stdout)
    
#    gather = 'SELECT * FROM ' + sql
#    mycursor.execute(gather)
#    mycursor.fetchall()
    
#    mycursor.execute(column, values)
    
#    mydb.commit()
    


def sql(table):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Smartgarden",
      database="SmartGarden"
    )
    mycursor = mydb.cursor()
    
    sql = 'SELECT * FROM ' + table
    mycursor.execute(sql)
    mycursor.fetchall() #This and the line above need to be used for the program to know how many rows their are.

    list_row = [] #Empty list for holding the row count
    
    list_row.append(mycursor.rowcount - 5) #Gives us a row count of the table which will be used inthe MYSQL statement below
    
    if list_row[0] < 0: #If statement to make sure the offset value given will not be a negative number
        list_row[0] = 0
    
    list_row = tuple(list_row) #The variable given in the below statement must be a tuple. This is all why a list was used initally and not a string or int
    
    
    sql = "SELECT * FROM " + table + " LIMIT 5 OFFSET %s" # MYSQL statement
    
    mycursor.execute(sql, list_row) #Statement that executes the MYSQL statement with the variable defined within.
    myresult = mycursor.fetchall() #fetchall gives us the answer from the MYSQL statement
    timelist = []
    templist = []
    
    sql = "SHOW columns FROM " + table
    mycursor.execute(sql)
    columns = mycursor.fetchall()
    
    columnlist = []
    
    for row in columns[2::]:
        columnlist.append(row[0])
    
    for row in list(myresult):
        timelist.append(row[1])
        listloop = list(row)
        listloop.pop(0)
        listloop.pop(0)
        templist.append(listloop)
    
    formatlist = []
    
    for i in range(len(templist[0])):
        formatlist.append([])
    
    for x in templist:
        count = 0
        for data in x:
            formatlist[count].append(data)
            count += 1
            
    return(timelist, formatlist, columnlist)

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/Charts')
def sensors():
    return render_template('charts.html');

@app.route('/BME280')
def smartgarden():
    table = 'BME280'
    timelist, formatlist, columnlist = sql(table)
    
    return render_template('BME280.html', time=timelist, temp=formatlist, column=columnlist);#For now the html page is given a list with tuples in it.
    
@app.route('/DS18B20')
def DS18B20():
    table = 'DS18B20'
    timelist, formatlist, columnlist = sql(table)
    
    return render_template('DS18B20.html', time=timelist, temp=formatlist, column=columnlist);#For now the html page is given a list with tuples in it.
  
@app.route('/SEN0114')
def SEN0114():
    table = 'SEN0114'
    timelist, formatlist, columnlist = sql(table)    
    
    return render_template('SEN0114.html', time=timelist, temp=formatlist, column=columnlist);#For now the html page is given a list with tuples in it.
    
@app.route('/SHT21')
def SHT21():
    table = 'SHT21'
    timelist, formatlist, columnlist = sql(table)
        
    return render_template('SHT21.html', time=timelist, temp=formatlist, column=columnlist);#For now the html page is given a list with tuples in it.
    
@app.route('/TSL2591')
def TSL2591():
    table = 'TSL2591'
    timelist, formatlist, columnlist = sql(table)      
        
    return render_template('TSL2591.html', time=timelist, temp=formatlist, column=columnlist);#For now the html page is given a list with tuples in it.

@app.route('/welcome.html')
def Welcome():
    return render_template('welcome.html')

@app.route('/add-project.html')
def AddProject():
    return render_template('add-project.html')

@app.route('/add-sensor.html')
def AddSesnor():
    return render_template('add-sensor.html')

@app.route('/sensors.html')
def Sesnor():
    return render_template('Sensors.html')


if __name__ == '__main__':
    app.run
    #app.run(debug=True, host='127.0.0.1', port=5020)
