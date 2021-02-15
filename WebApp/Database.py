##Code taken from https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
#db.create_all()


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f"latest(id={id}, username={username}, email={email})"

resource_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String
}

#row1 = (id=1, username='Sam', email="s.gib@hot.co.uk")
#row2 = user(id=2, username='Gibson', email="40429@nap.ac.uk")

#db.session.add(row1)
#db.session.commit()
