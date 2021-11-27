from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from enum import Enum


class predictionForm(FlaskForm):
    name = StringField('Name of restaurant', validators=[DataRequired()])
    # online_order = StringField('Online Order', validators=[DataRequired()])
    # book_table = StringField('Booking Table is available ?', validators=[DataRequired()])
    # votes = IntegerField('Votes', validators=[DataRequired()])
    # location = StringField('Location of Restaurant', validators=[DataRequired()])
    # rest_type = StringField('Restaurant type', validators=[DataRequired()])
    # cuisines = StringField('Cusines', validators=[DataRequired()])
    # cost = StringField('Cost', validators=[DataRequired()])
    # menu_item = StringField('Menu Item', validators=[DataRequired()])
    # type = StringField('Type of Serving', validators=[DataRequired()])
    submit = SubmitField('Press here to find the rating')


