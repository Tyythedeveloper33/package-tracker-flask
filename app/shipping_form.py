from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from app.map.map import map

class ShippingForm(FlaskForm):
    # Create the choices list
    cities = [(city, city) for city in sorted(map.keys())]

    sender = StringField('Sender', validators=[DataRequired()])
    recipient = StringField('Recipient', validators=[DataRequired()])
    # Assign choices to the SelectFields
    origin = SelectField('Origin', choices=cities)
    destination = SelectField('Destination', choices=cities)
    express = BooleanField('Express Shipping')
    location = StringField('Location' )
    submit = SubmitField('Submit')
