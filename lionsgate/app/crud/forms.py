import re
from flask_wtf import FlaskForm
from wtforms import StringField, \
                    SubmitField, \
                    DateField, \
                    IntegerField, \
                    FloatField, \
                    BooleanField, \
                    TextAreaField, \
                    SelectField, \
                    SelectMultipleField, \
                    RadioField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Optional, ValidationError, Email, Length
from models import Station


class StationForm(FlaskForm):
    code = StringField('Code', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SensorForm(FlaskForm):
    id = IntegerField('Id')
    station_code = StringField('Station code', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    manufacturer = StringField('Manufacturer')
    part_no = StringField('Part No.')
    url = StringField('URL')
    notes_text = TextAreaField('Notes')
    submit = SubmitField('Submit')
