from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, SelectField, DateTimeLocalField, SubmitField
from wtforms.validators import DataRequired, Email
from models import categories, subcategories

class BookingForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = TelField('Phone Number', validators=[DataRequired()])
    category = SelectField('Treatment Category', choices=[], validators=[DataRequired()])
    subcategory = SelectField('Treatment Subcategory', choices=[], validators=[DataRequired()])
    appointment = DateTimeLocalField('Appointment Date & Time', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    submit = SubmitField('Book Now')