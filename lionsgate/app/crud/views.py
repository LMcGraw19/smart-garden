from flask import abort, flash, redirect, render_template, url_for, current_app, request
# from flask_login import current_user, login_required
from sqlalchemy import desc
from sqlalchemy.sql import text, func
from datetime import timedelta

import json

from . import crud
from .forms import *
from models import *
# from app.common import get_this_year, change_academic_year, sanitise

# def check_admin():
#     if not current_user.is_admin:
#         abort(403)


@crud.route('/crud/stations', methods=['GET', 'POST'])
# @login_required
def stations():
    # check_admin()
    stations = Station.query.all()
    return render_template('crud/stations.html', stations=stations, title="Stations")

@crud.route('/crud/station/', methods=['GET', 'POST'])
# @login_required
def add_station():
    # check_admin()
    create_record = True

    form = StationForm()
    if form.validate_on_submit():
        station = Station(code=form.code.data,
                          name=form.name.data)
        try:
            db.session.add(station)
            db.session.commit()
            flash('You have successfully added a new station.')
        except:
            flash('Error: station already exists.')

        return redirect(url_for('crud.stations'))

    return render_template('crud/station.html', action="Add",
                           create_record=create_record, form=form,
                           title="New Station",
                           object_type='Station')

@crud.route('/crud/station/<code>', methods=['GET', 'POST'])
# @login_required
def edit_station(code):
    # check_admin()
    create_record = False

    station = Station.query.get_or_404(code)
    form = StationForm(obj=station)
    if form.validate_on_submit():
        station.code = form.code.data
        station.name = form.name.data
        db.session.commit()
        flash('You have successfully edited the station')

        return redirect(url_for('crud.stations'))

    # form = StationForm(obj=station)
    return render_template('crud/station.html', action="Edit",
                           create_record=create_record, form=form,
                           station=station, title="Edit Station")


@crud.route('/crud/delete_station/<code>', methods=['GET', 'POST'])
# @login_required
def delete_station(code):
    # check_admin()

    station = Station.query.get_or_404(code)
    try:
        db.session.delete(station)
        db.session.commit()
        flash('You have successfully deleted a station.')
    except:
        flash('Error deleting station.')

    return redirect(url_for('crud.stations'))


@crud.route('/crud/sensors', methods=['GET', 'POST'])
# @login_required
def sensors():
    # check_admin()
    sensors = Sensor.query.all()
    return render_template('crud/sensors.html', sensors=sensors, title="Sensors")


@crud.route('/crud/sensor/', methods=['GET', 'POST'])
# @login_required
def add_sensor():
    # check_admin()
    create_record = True

    form = SensorForm()
    if form.validate_on_submit():
        sensor = Sensor(id=form.id.data,
                        station_code=form.station_code.data,
                        name=form.name.data,
                        type=form.type.data,
                        manufacturer=form.manufacturer.data,
                        part_no=form.part_no.data,
                        url=form.url.data,
                        notes_text=form.notes_text.data
                        )
        try:
            db.session.add(sensor)
            db.session.commit()
            flash('You have successfully added a new sensor.')
        except:
            flash('Error: sensor already exists.')

        return redirect(url_for('crud.sensors'))

    return render_template('crud/sensor.html', action="Add",
                           create_record=create_record, form=form,
                           title="New Sensor",)

@crud.route('/crud/sensor/<id>', methods=['GET', 'POST'])
# @login_required
def edit_sensor(id):
    # check_admin()
    create_record = False

    sensor = Sensor.query.get_or_404(id)
    form = SensorForm(obj=sensor)
    if form.validate_on_submit():
        sensor.id = form.id.data
        sensor.station_code = form.station_code.data
        sensor.name = form.name.data
        sensor.type = form.type.data
        sensor.manufacturer = form.manufacturer.data
        sensor.part_no = form.part_no.data
        sensor.url = form.url.data
        sensor.notes_text = form.notes_text.data
        db.session.commit()
        flash('You have successfully edited the sensor')

        return redirect(url_for('crud.sensors'))

    # form = StationForm(obj=station)
    return render_template('crud/sensor.html', action="Edit",
                           create_record=create_record, form=form,
                           station=sensor, title="Edit Sensor")


@crud.route('/crud/delete_sensor/<id>', methods=['GET', 'POST'])
# @login_required
def delete_sensor(id):
    # check_admin()

    sensor = Sensor.query.get_or_404(id)
    try:
        db.session.delete(sensor)
        db.session.commit()
        flash('You have successfully deleted a sensor.')
    except:
        flash('Error deleting sensor.')

    return redirect(url_for('crud.sensors'))


@crud.route('/crud/station_data/<code>', methods=['GET', 'POST'])
# @login_required
def station_data(code):
    # check_admin()

    station = Station.query.filter(Station.code == code).first()
    data = Data.query.join(Data.sensor).join(Sensor.station).all()
    return render_template('crud/data.html', data=data, title=station.name)


@crud.route('/crud/sensor_data/<id>', methods=['GET', 'POST'])
# @login_required
def sensor_data(id):
    # check_admin()

    sensor = Sensor.query.filter(Sensor.id == id).first()
    title = "{} {}".format(sensor.station.name, sensor.name)
    data = Data.query.join(Data.sensor).filter(Data.sensor_id==sensor.id).all()
    return render_template('crud/data.html', data=data, title=title)

