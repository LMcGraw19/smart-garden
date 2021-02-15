from flask import Flask, request, render_template
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartgarden.db'
db = SQLAlchemy(app)

class Temp(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    Temp = db.Column(db.Integer)
    Humidity = db.Column(db.Integer)
    
    def _repr__(self):
        return f"latest(temp={Temp}, water={Humidity})"

db.create_all()


names ={"Temp": {"age": 29, "gender": "male"},
        "bill": {"age": 40, "gender": "male"}}

videos = {}

class Hello(Resource):
    def get(self, name):
        return names[name]
    
    def post(self):
        return{"data": "Hello World"}

api.add_resource(Hello, "/<string:name>")

@app.route('/')
def home():
    return render_template('welcome.html');

@app.route('/smartgarden')
def smartgarden():
    return render_template('smartgarden.html');
    
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host='127.0.0.1', port=5020)
