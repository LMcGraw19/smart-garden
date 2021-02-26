from flask import render_template, url_for, request

from . import api
from sqlalchemy import and_, exc
import json
from models import *
import logging
logger = logging.getLogger()

@api.route('/api/store/', methods=['GET', 'POST'])
def store():

    try:
        reading = json.loads(request.data)
        data = json.loads(reading['data'])
        # data = reading['data']
    except:
        reading = "No valid JSON data found"
        data = {"sensors": [{"name": "Dummy"},]}

    try:
        for sensor in data['sensors']:
            sensor_id = Sensor.query.filter(and_(Sensor.name == sensor['name'], Sensor.station_code == data['station'])).first().id
            datum = Data(
                sensor_id=sensor_id,
                timestamp=datetime.now(),
                value=sensor['value']
            )
            db.session.add(datum)
            db.session.commit()
        return 'OK'
    except (exc.SQLAlchemyError, exc.DBAPIError) as e:
        return e
    except:
        return data


@api.route('/api/station_data/<code>', methods=['GET', 'POST'])
def station_data(code):

    return_object = {
        'station': code,
        'sensors': []
    }

    sensors = Sensor.query.filter(Sensor.station_code==code).all()
    for sensor in sensors:
        sensor_object = {
            'name': sensor.name,
            'labels': [],
            'values': []
        }
        data = Data.query.filter(Data.sensor_id==sensor.id).all()
        for d in data:
            sensor_object['labels'].append(str(d.timestamp))
            sensor_object['values'].append(d.value)

        return_object['sensors'].append(sensor_object)

    return json.dumps(return_object)

@api.route('/api/sensor_data/<id>', methods=['GET', 'POST'])
def sensor_data(id):

    try:
        sensor = Sensor.query.filter(Sensor.id==id).first()

        return_object = {
            'station': sensor.station_code,
            'sensors': [
                {
                    'name': sensor.name,
                    'labels': [],
                    'values': []
                }
            ]
        }

        data = Data.query.filter(Data.sensor_id==sensor.id).all()
        for d in data:
            return_object['sensors'][0]['labels'].append(str(d.timestamp))
            return_object['sensors'][0]['values'].append(d.value)

        return json.dumps(return_object)
    except (exc.SQLAlchemyError, exc.DBAPIError) as e:
        return e

@api.route('/api/chart/test1', methods=['GET', 'POST'])
def test1():
    title = "Test chart 1"
    return render_template('charts/test1.html', title=title)
