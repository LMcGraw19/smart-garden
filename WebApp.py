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
def home():
    return render_template('welcome.html');

@app.route('/smartgarden')
def smartgarden():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="SmartGarden"
    )

    mycursor = mydb.cursor()
    
    mycursor.execute('SELECT * FROM air_temperature')
    mycursor.fetchall() #This and the line above need to be used for the program to know how many rows their are.
    
    list_row = [] #Empty list for holding the row count
    
    list_row.append(mycursor.rowcount - 5) #Gives us a row count of the table which will be used inthe MYSQL statement below
    
    if list_row[0] < 0: #If statement to make sure the offset value given will not be a negative number
        list_row[0] = 0
    
    list_row = tuple(list_row) #The variable given in the below statement must be a tuple. This is all why a list was used initally and not a string or int
    
    
    sql = "SELECT * FROM air_temperature LIMIT 5 OFFSET %s" # MYSQL statement
    
    mycursor.execute(sql, list_row) #Statement that executes the MYSQL statement with the variable defined within.

    myresult = list(mycursor.fetchall()) #fetchall gives us the answer from the MYSQL statement
    
    return render_template('smartgarden.html', test=myresult); #For now the html page is given a list with tuples in it.
    
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host='127.0.0.1', port=5020)
