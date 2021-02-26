from datetime import datetime
# from flask_login import UserMixin
# from sqlalchemy import and_
# from sqlalchemy.orm import relationship
# from werkzeug.security import generate_password_hash, check_password_hash, pbkdf2_hex
from flask_sqlalchemy import SQLAlchemy

from app import db


class Station(db.Model):
    __tablename__ = 'station'

    code = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(50))
    sensors = db.relationship('Sensor', backref='station', lazy='joined', cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Station: {} ({})>'.format(self.name, self.code)


class Sensor(db.Model):
    __tablename__ = 'sensor'

    id = db.Column(db.Integer, primary_key=True)
    station_code = db.Column(db.String(8), db.ForeignKey('station.code'), nullable=False, index=True)
    name = db.Column(db.String(30), nullable=False)
    type = db.Column(db.String(30), nullable=False)
    manufacturer = db.Column(db.String(30), nullable=True)
    part_no = db.Column(db.String(30), nullable=True)
    url = db.Column(db.String(255), nullable=True)
    notes_text = db.Column(db.Text, nullable=True)
    data = db.relationship('Data', backref='sensor', lazy='joined', cascade="all, delete", passive_deletes=True)


    def __repr__(self):
        return '<Sensor: {} {} on {} station>'.format(self.name, self.type, self.station_code)


class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False, index=True)
    timestamp = db.Column(db.DateTime, nullable=False, index=True, default=datetime.now())
    value = db.Column(db.Float)

    def __repr__(self):
        return '<Data: {} {}>'.format(self.timestamp, self.value)
